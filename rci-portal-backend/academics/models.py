import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator

#==========================================
# 1. USERS TABLE
#==========================================

class User(AbstractUser):
    ROLE_CHOICES = [
        ('student', 'Student'),
        ('registrar', 'Registrar'),
        ('admissions', 'Admission'),
        ('head', 'Head'),
        ('professor', 'Professor'),
        ('admin', 'Admin'),
    ]

   # Note: These are inherited from AbstractUser :
    # - username: CharField (inherited, unique=True)
    # - password: CharField (inherited, auto-hashed by Django)
    # - date_joined: DateTimeField (inherited, auto_now_add=True)
    # - is_active: BooleanField (inherited, default=True)


    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    email = models.EmailField(unique=True)
    

    class Meta:
        db_table = 'users'
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"



#==========================================
# 2. PROGRAMS TABLE
#==========================================

class Program(models.Model):
    program_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program_code = models.CharField(max_length=10, unique=True)
    program_name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)

    class Meta:
        db_table = 'programs'
        ordering = ['program_code']
    
    def __str__(self):
        return f"{self.program_code} - {self.program_name}"
    
#==========================================
# 3. CURRICULUM TABLE
#==========================================

class Curriculum(models.Model):
    SEMESTER_CHOICES = [
        ('1st', '1st Semester'),
        ('2nd', '2nd Semester'),
        ('Summer', 'Summer Term'),
    ]

    curriculum_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    program = models.ForeignKey(Program, on_delete=models.CASCADE, related_name='curriculums')
    year_level = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])
    semester = models.CharField(max_length=10, choices=SEMESTER_CHOICES)

    class Meta:
        db_table = 'curriculums'
        unique_together = ('program', 'year_level', 'semester')
        ordering = ['program', 'year_level', 'semester']

    def __str__(self):
        return f"{self.program.program_code} - Year {self.year_level} {self.semester}"
    

#==========================================
# 4. SUBJECTS TABLE
#==========================================

class Subject(models.Model):

    subject_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    code = models.CharField(max_length=10, unique=True)
    title = models.CharField(max_length=200)
    units = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    prerequisites = models.JSONField(default=list, blank=True)
    syllabus_pdf = models.FileField(upload_to='syllabi/', null=True, blank=True)
    curriculum = models.ForeignKey(Curriculum, on_delete=models.CASCADE, related_name='subjects')
    summary = models.TextField(blank=True)

    class Meta:
        db_table = 'subjects'
        ordering = ['code']
    
    def __str__(self):
        return f"{self.code} - {self.title}"
    

#==========================================
# 5. SECTIONS TABLE
#==========================================

class Section(models.Model):
    section_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    section_name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='sections')
    term = models.CharField(max_length=20)
    schedule = models.CharField(max_length=100)
    room = models.CharField(max_length=50)
    professor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'role': 'professor'}, related_name='teaching_sections')

    class Meta:
        db_table = 'sections'
        ordering = ['term', 'subject__code']
    
    def __str__(self):
        return f"{self.subject.code} - {self.term} - {self.room}"

#==========================================
# 6. STUDENTS TABLE
#==========================================

class Student(models.Model):

    STATUS_CHOICES = [
        ('enrolled', 'Enrolled'),
        ('graduated', 'Graduated'),
        ('dropped', 'Dropped'),
        ('loa', 'Leave of Absence'),
    ]

    student_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
    student_number = models.CharField(max_length=20, unique=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='enrolled')
    program = models.ForeignKey(Program, on_delete=models.PROTECT, related_name='students')
    year_level = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(4)])

    class Meta:
        db_table = 'students'
        ordering = ['student_number']
    
    def __str__(self):
        return f"{self.student_number} - {self.user.get_full_name()}"
    

#==========================================
# 7. ENROLLMENTS TABLE
#==========================================

class Enrollment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('enrolled', 'Enrolled'),
        ('dropped', 'Dropped'),
    ]
    enrollment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='enrollments')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='enrollments')
    term = models.CharField(max_length=20)
    status = models.CharField(max_length=20, choices= STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'enrollments'
        unique_together = ('student', 'section', 'term')
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.student.student_number} enrolled in {self.section.subject.code} - {self.status}"
    
#==========================================
# 8. GRADES TABLE
#==========================================

class Grade(models.Model):
    STATUS_CHOICES = [
        ('passed', 'Passed'),
        ('failed', 'Failed'),
        ('inc', 'Incomplete'),
    ]

    grade_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='grades')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='grades')
    section = models.ForeignKey(Section, on_delete=models.CASCADE, related_name='grades')
    grade = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    encoded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='encoded_grades')
    signatories = models.JSONField(default=dict, blank=True)



    class Meta:
        db_table = 'grades'
        unique_together = ('student', 'subject', 'section')
        ordering = ['-section__term']
    
    def __str__(self):
        return f"{self.student.student_number} - {self.subject.code}: {self.grade or 'INC'}"
    
#==========================================
# 9. APPLICATIONS TABLE
#==========================================

class Application(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    application_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    applicant_name = models.CharField(max_length=100)
    email = models.EmailField()
    program = models.ForeignKey(Program, on_delete=models.PROTECT, related_name='applications')
    uploaded_requirements = models.JSONField(default=list, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'applications'
        ordering = ['-timestamp']
    
    def __str__(self):
        return f"{self.applicant_name} - {self.program.program_code} ({self.status})"
    

#==========================================
# 10. DOCUMENTS TABLE
#==========================================.

class Document(models.Model):

    DOC_TYPE_CHOICES = [
        ('tor', 'Transcript of Records'),
        ('cor', 'Certificate of Registration'),
        ('diploma', 'Diploma'),
        ('clearance', 'Clearance'),
        ('id', 'ID Document'),
        ('others', 'Others'),
    ]

    document_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='documents', null=True, blank=True)
    doc_type = models.CharField(max_length=20, choices=DOC_TYPE_CHOICES)
    file_path = models.FileField(upload_to='documents/')
    uploaded_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='uploaded_documents')
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        db_table = 'documents'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.get_doc_type_display()} - {self.student.student_number if self.student else 'N/A'}"
    
    

#==========================================
# 11. AUDIT LOGS TABLE
#==========================================

class AuditLog(models.Model):

    ACTION_CHOICES = [
        ('create', 'Create'),
        ('update', 'Update'),
        ('delete', 'Delete'),
    ]

    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entity = models.CharField(max_length=50)
    action = models.CharField(max_length=20, choices=ACTION_CHOICES)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='audit_logs')
    details = models.JSONField(default=dict)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'audit_logs'
        ordering = ['-timestamp']

    def __str__(self):
        return f"{self.action} on {self.entity} by {self.user.username if self.user else 'System'}"
    