# academics/serializers.py

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import (
    User, Program, Curriculum, Subject, Section,
    Student, Enrollment, Grade, Application, Document, AuditLog
)

# ========================================
# USER & AUTHENTICATION SERIALIZERS
# ========================================

class UserSerializer(serializers.ModelSerializer):
    """Serialize User data (excluding password)"""
    full_name = serializers.SerializerMethodField()
    
    class Meta:
        model = User
        fields = ['user_id', 'username', 'email', 'role', 'first_name', 
                  'last_name', 'full_name', 'is_active', 'date_joined']
        read_only_fields = ['user_id', 'date_joined']
    
    def get_full_name(self, obj):
        return obj.get_full_name()


class UserCreateSerializer(serializers.ModelSerializer):
    """Create new users with password handling"""
    password = serializers.CharField(write_only=True, min_length=8)
    password_confirm = serializers.CharField(write_only=True)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password_confirm', 
                  'role', 'first_name', 'last_name']
    
    def validate(self, data):
        # Check passwords match
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError("Passwords do not match")
        return data
    
    def create(self, validated_data):
        # Remove password_confirm before creating user
        validated_data.pop('password_confirm')
        
        # Use create_user to properly hash password
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    """Handle user login"""
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        username = data.get('username')
        password = data.get('password')
        
        if username and password:
            user = authenticate(username=username, password=password)
            
            if not user:
                raise serializers.ValidationError("Invalid username or password")
            
            if not user.is_active:
                raise serializers.ValidationError("User account is disabled")
            
            data['user'] = user
            return data
        else:
            raise serializers.ValidationError("Must include username and password")


class ChangePasswordSerializer(serializers.Serializer):
    """Change user password"""
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True, min_length=8)
    new_password_confirm = serializers.CharField(write_only=True)
    
    def validate(self, data):
        if data['new_password'] != data['new_password_confirm']:
            raise serializers.ValidationError("New passwords do not match")
        return data


# ========================================
# PROGRAM & CURRICULUM SERIALIZERS
# ========================================

class ProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = Program
        fields = '__all__'
        read_only_fields = ['program_id']


class SubjectSerializer(serializers.ModelSerializer):
    curriculum_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Subject
        fields = '__all__'
        read_only_fields = ['subject_id']
    
    def get_curriculum_info(self, obj):
        return {
            'program': obj.curriculum.program.program_code,
            'year_level': obj.curriculum.year_level,
            'semester': obj.curriculum.semester
        }


class CurriculumSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.program_name', read_only=True)
    program_code = serializers.CharField(source='program.program_code', read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    
    class Meta:
        model = Curriculum
        fields = '__all__'
        read_only_fields = ['curriculum_id']


# ========================================
# SECTION SERIALIZERS
# ========================================

class SectionSerializer(serializers.ModelSerializer):
    subject_code = serializers.CharField(source='subject.code', read_only=True)
    subject_title = serializers.CharField(source='subject.title', read_only=True)
    professor_name = serializers.CharField(source='professor.get_full_name', read_only=True)
    enrolled_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Section
        fields = '__all__'
        read_only_fields = ['section_id']
    
    def get_enrolled_count(self, obj):
        return obj.enrollments.filter(status='enrolled').count()


# ========================================
# STUDENT SERIALIZERS
# ========================================

class StudentSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='user', read_only=True)
    program_name = serializers.CharField(source='program.program_name', read_only=True)
    program_code = serializers.CharField(source='program.program_code', read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ['student_id']


class StudentCreateSerializer(serializers.ModelSerializer):
    user_info = UserSerializer(source='user', read_only=True)
    
    class Meta:
        model = Student
        fields = ['user', 'user_info', 'student_number', 'program', 'year_level', 'status']
    
    def validate_user(self, value):
        if value.role != 'student':
            raise serializers.ValidationError("User must have 'student' role")
        if hasattr(value, 'student_profile'):
            raise serializers.ValidationError("Student profile already exists for this user")
        return value


# ========================================
# ENROLLMENT SERIALIZERS
# ========================================

class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    student_number = serializers.CharField(source='student.student_number', read_only=True)
    section_info = SectionSerializer(source='section', read_only=True)
    
    class Meta:
        model = Enrollment
        fields = '__all__'
        read_only_fields = ['enrollment_id', 'timestamp']


class EnrollmentCreateSerializer(serializers.ModelSerializer):
    """Create enrollment with prerequisite validation"""
    
    class Meta:
        model = Enrollment
        fields = ['student', 'section', 'term', 'status']
    
    def validate(self, data):
        student = data['student']
        section = data['section']
        subject = section.subject
        
        # Check prerequisites
        if subject.prerequisites:
            for prereq_id in subject.prerequisites:
                # Check if student has passed the prerequisite
                passed = Grade.objects.filter(
                    student=student,
                    subject__subject_id=prereq_id,
                    status='passed'
                ).exists()
                
                if not passed:
                    prereq = Subject.objects.get(subject_id=prereq_id)
                    raise serializers.ValidationError(
                        f"Prerequisite not met: {prereq.code} - {prereq.title}"
                    )
        
        # Check for duplicate enrollment
        duplicate = Enrollment.objects.filter(
            student=student,
            section=section,
            term=data['term']
        ).exists()
        
        if duplicate:
            raise serializers.ValidationError(
                "Student is already enrolled in this section for this term"
            )
        
        return data


# ========================================
# GRADE SERIALIZERS
# ========================================

class GradeSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    student_number = serializers.CharField(source='student.student_number', read_only=True)
    subject_code = serializers.CharField(source='subject.code', read_only=True)
    subject_title = serializers.CharField(source='subject.title', read_only=True)
    encoded_by_name = serializers.CharField(source='encoded_by.get_full_name', read_only=True)
    
    class Meta:
        model = Grade
        fields = '__all__'
        read_only_fields = ['grade_id']


class GradeSubmitSerializer(serializers.ModelSerializer):
    """Professor submits/updates grades"""
    
    class Meta:
        model = Grade
        fields = ['student', 'subject', 'section', 'grade', 'status', 'signatories']
        
    def validate(self, data):
        # If grade is provided, status cannot be 'inc'
        if data.get('grade') and data.get('status') == 'inc':
            raise serializers.ValidationError(
                "Cannot set status to INC when grade is provided"
            )
        
        # If status is passed/failed, grade must be provided
        if data.get('status') in ['passed', 'failed'] and not data.get('grade'):
            raise serializers.ValidationError(
                "Grade is required for passed/failed status"
            )
        
        return data
    
    def create(self, validated_data):
        # Set encoded_by to current user
        validated_data['encoded_by'] = self.context['request'].user
        return super().create(validated_data)


# ========================================
# APPLICATION SERIALIZERS
# ========================================

class ApplicationSerializer(serializers.ModelSerializer):
    program_name = serializers.CharField(source='program.program_name', read_only=True)
    program_code = serializers.CharField(source='program.program_code', read_only=True)
    
    class Meta:
        model = Application
        fields = '__all__'
        read_only_fields = ['application_id', 'timestamp']


# ========================================
# DOCUMENT SERIALIZERS
# ========================================

class DocumentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.user.get_full_name', read_only=True)
    student_number = serializers.CharField(source='student.student_number', read_only=True)
    uploaded_by_name = serializers.CharField(source='uploaded_by.get_full_name', read_only=True)
    
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ['document_id', 'timestamp']


# ========================================
# AUDIT LOG SERIALIZERS
# ========================================

class AuditLogSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    user_role = serializers.CharField(source='user.role', read_only=True)
    
    class Meta:
        model = AuditLog
        fields = '__all__'
        read_only_fields = ['log_id', 'timestamp']