# academics/views.py

from rest_framework import viewsets, status, generics
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import logout

from .models import (
    User, Program, Curriculum, Subject, Section,
    Student, Enrollment, Grade, Application, Document, AuditLog
)
from .serializers import (
    UserSerializer, UserCreateSerializer, LoginSerializer, ChangePasswordSerializer,
    ProgramSerializer, CurriculumSerializer, SubjectSerializer, SectionSerializer,
    StudentSerializer, StudentCreateSerializer, EnrollmentSerializer, EnrollmentCreateSerializer,
    GradeSerializer, GradeSubmitSerializer, ApplicationSerializer, 
    DocumentSerializer, AuditLogSerializer
)
from .permissions import (
    IsAdmin, IsRegistrar, IsAdmission, IsHead, IsProfessor, IsStudent,
    IsAdminOrRegistrar, IsAdminOrHead, IsStaffUser, IsOwnerOrStaff,
    CanManageGrades, CanEnroll, ReadOnlyOrStaff, CanManageCurriculum,
    CanManageApplications, CanViewAnalytics
)

# ========================================
# AUTHENTICATION VIEWS
# ========================================

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Custom JWT token with additional user info"""
    
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # Add custom claims
        token['username'] = user.username
        token['email'] = user.email
        token['role'] = user.role
        token['full_name'] = user.get_full_name()
        
        return token
    
    def validate(self, attrs):
        data = super().validate(attrs)
        
        # Add extra user info to response
        data['user'] = {
            'user_id': str(self.user.user_id),
            'username': self.user.username,
            'email': self.user.email,
            'role': self.user.role,
            'full_name': self.user.get_full_name(),
        }
        
        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    """Custom login endpoint that returns JWT tokens with user info"""
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register_view(request):
    """Register a new user"""
    serializer = UserCreateSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        
        # Generate tokens for the new user
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'User created successfully',
            'user': UserSerializer(user).data,
            'tokens': {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }
        }, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    """Logout user by blacklisting refresh token"""
    try:
        refresh_token = request.data.get('refresh_token')
        token = RefreshToken(refresh_token)
        token.blacklist()  # Add token to blacklist
        
        return Response({
            'message': 'Logged out successfully'
        }, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({
            'error': 'Invalid token'
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def current_user_view(request):
    """Get current logged-in user info"""
    serializer = UserSerializer(request.user)
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def change_password_view(request):
    """Change user password"""
    serializer = ChangePasswordSerializer(data=request.data)
    
    if serializer.is_valid():
        user = request.user
        
        # Check old password
        if not user.check_password(serializer.validated_data['old_password']):
            return Response({
                'error': 'Old password is incorrect'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Set new password
        user.set_password(serializer.validated_data['new_password'])
        user.save()
        
        return Response({
            'message': 'Password changed successfully'
        }, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ========================================
# USER MANAGEMENT VIEWSET
# ========================================

class UserViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for users.
    Only admins can create/update/delete users.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def get_queryset(self):
        """Filter users based on role"""
        queryset = User.objects.all()
        
        # Filter by role if provided
        role = self.request.query_params.get('role', None)
        if role:
            queryset = queryset.filter(role=role)
        
        # Filter by active status
        is_active = self.request.query_params.get('is_active', None)
        if is_active is not None:
            queryset = queryset.filter(is_active=is_active.lower() == 'true')
        
        return queryset
    
    @action(detail=True, methods=['post'])
    def deactivate(self, request, pk=None):
        """Deactivate a user account"""
        user = self.get_object()
        user.is_active = False
        user.save()
        return Response({'message': 'User deactivated successfully'})
    
    @action(detail=True, methods=['post'])
    def activate(self, request, pk=None):
        """Activate a user account"""
        user = self.get_object()
        user.is_active = True
        user.save()
        return Response({'message': 'User activated successfully'})


# ========================================
# PROGRAM & CURRICULUM VIEWSETS
# ========================================

class ProgramViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for programs.
    Admins and heads can manage, others can view.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrStaff]
    
    def get_queryset(self):
        queryset = Program.objects.all()
        
        # Filter by department
        department = self.request.query_params.get('department', None)
        if department:
            queryset = queryset.filter(department=department)
        
        # Filter by sector
        sector = self.request.query_params.get('sector', None)
        if sector:
            queryset = queryset.filter(sector=sector)
        
        return queryset


class CurriculumViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for curriculum.
    Admins and heads can manage, others can view.
    """
    queryset = Curriculum.objects.all()
    serializer_class = CurriculumSerializer
    permission_classes = [IsAuthenticated, CanManageCurriculum]
    
    def get_queryset(self):
        queryset = Curriculum.objects.select_related('program').prefetch_related('subjects')
        
        # Filter by program
        program_id = self.request.query_params.get('program', None)
        if program_id:
            queryset = queryset.filter(program__program_id=program_id)
        
        # Filter by year level
        year_level = self.request.query_params.get('year_level', None)
        if year_level:
            queryset = queryset.filter(year_level=year_level)
        
        return queryset


class SubjectViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for subjects.
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrStaff]
    
    def get_queryset(self):
        queryset = Subject.objects.select_related('curriculum__program')
        
        # Filter by curriculum
        curriculum_id = self.request.query_params.get('curriculum', None)
        if curriculum_id:
            queryset = queryset.filter(curriculum__curriculum_id=curriculum_id)
        
        # Filter by subject code
        code = self.request.query_params.get('code', None)
        if code:
            queryset = queryset.filter(code__icontains=code)
        
        return queryset


class SectionViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for sections.
    """
    queryset = Section.objects.all()
    serializer_class = SectionSerializer
    permission_classes = [IsAuthenticated, ReadOnlyOrStaff]
    
    def get_queryset(self):
        queryset = Section.objects.select_related('subject', 'professor')
        
        # Filter by term
        term = self.request.query_params.get('term', None)
        if term:
            queryset = queryset.filter(term=term)
        
        # Filter by professor
        professor_id = self.request.query_params.get('professor', None)
        if professor_id:
            queryset = queryset.filter(professor__user_id=professor_id)
        
        # Professors see only their sections
        if self.request.user.role == 'professor':
            queryset = queryset.filter(professor=self.request.user)
        
        return queryset


# ========================================
# STUDENT VIEWSETS
# ========================================

class StudentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for student profiles.
    """
    queryset = Student.objects.all()
    permission_classes = [IsAuthenticated, IsAdminOrRegistrar]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return StudentCreateSerializer
        return StudentSerializer
    
    def get_queryset(self):
        queryset = Student.objects.select_related('user', 'program')
        
        # Filter by program
        program_id = self.request.query_params.get('program', None)
        if program_id:
            queryset = queryset.filter(program__program_id=program_id)
        
        # Filter by year level
        year_level = self.request.query_params.get('year_level', None)
        if year_level:
            queryset = queryset.filter(year_level=year_level)
        
        # Filter by status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        
        # Students can only see their own profile
        if self.request.user.role == 'student':
            queryset = queryset.filter(user=self.request.user)
        
        return queryset


# ========================================
# ENROLLMENT VIEWSETS
# ========================================

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for enrollments with prerequisite validation.
    """
    queryset = Enrollment.objects.all()
    permission_classes = [IsAuthenticated, CanEnroll]
    
    def get_serializer_class(self):
        if self.action == 'create':
            return EnrollmentCreateSerializer
        return EnrollmentSerializer
    
    def get_queryset(self):
        queryset = Enrollment.objects.select_related(
            'student__user', 'student__program', 'section__subject', 'section__professor'
        )
        
        # Filter by student
        student_id = self.request.query_params.get('student', None)
        if student_id:
            queryset = queryset.filter(student__student_id=student_id)
        
        # Filter by term
        term = self.request.query_params.get('term', None)
        if term:
            queryset = queryset.filter(term=term)
        
        # Filter by status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        
        # Students see only their own enrollments
        if self.request.user.role == 'student':
            queryset = queryset.filter(student__user=self.request.user)
        
        # Professors see enrollments in their sections
        elif self.request.user.role == 'professor':
            queryset = queryset.filter(section__professor=self.request.user)
        
        return queryset


# ========================================
# GRADE VIEWSETS
# ========================================

class GradeViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for grades.
    Professors can submit grades for their sections.
    """
    queryset = Grade.objects.all()
    permission_classes = [IsAuthenticated, CanManageGrades]
    
    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return GradeSubmitSerializer
        return GradeSerializer
    
    def get_queryset(self):
        queryset = Grade.objects.select_related(
            'student__user', 'subject', 'section', 'encoded_by'
        )
        
        # Filter by student
        student_id = self.request.query_params.get('student', None)
        if student_id:
            queryset = queryset.filter(student__student_id=student_id)
        
        # Filter by subject
        subject_id = self.request.query_params.get('subject', None)
        if subject_id:
            queryset = queryset.filter(subject__subject_id=subject_id)
        
        # Filter by status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        
        # Students see only their own grades
        if self.request.user.role == 'student':
            queryset = queryset.filter(student__user=self.request.user)
        
        # Professors see grades for their sections only
        elif self.request.user.role == 'professor':
            queryset = queryset.filter(section__professor=self.request.user)
        
        return queryset


# ========================================
# APPLICATION VIEWSETS
# ========================================

class ApplicationViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for admission applications.
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [IsAuthenticated, CanManageApplications]
    
    def get_queryset(self):
        queryset = Application.objects.select_related('program')
        
        # Filter by program
        program_id = self.request.query_params.get('program', None)
        if program_id:
            queryset = queryset.filter(program__program_id=program_id)
        
        # Filter by status
        status = self.request.query_params.get('status', None)
        if status:
            queryset = queryset.filter(status=status)
        
        return queryset


# ========================================
# DOCUMENT VIEWSETS
# ========================================

class DocumentViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for documents.
    """
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer
    permission_classes = [IsAuthenticated, IsAdminOrRegistrar]
    
    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


# ========================================
# AUDIT LOG VIEWSETS
# ========================================

class AuditLogViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Read-only access to audit logs.
    Only admins can view audit logs.
    """
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer
    permission_classes = [IsAuthenticated, IsAdmin]
    
    def get_queryset(self):
        queryset = AuditLog.objects.select_related('user').order_by('-timestamp')
        
        # Filter by entity
        entity = self.request.query_params.get('entity', None)
        if entity:
            queryset = queryset.filter(entity__icontains=entity)
        
        # Filter by action
        action = self.request.query_params.get('action', None)
        if action:
            queryset = queryset.filter(action=action)
        
        # Filter by user
        user_id = self.request.query_params.get('user', None)
        if user_id:
            queryset = queryset.filter(user__user_id=user_id)
        
        return queryset