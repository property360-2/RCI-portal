# ============================================
# FILE: rci-portal-backend/setup_test_data.py
# ============================================
"""
Complete Test Data Setup Script
Run this to populate your database with test users and data

Usage:
    python manage.py shell < setup_test_data.py
    
Or:
    python manage.py shell
    >>> exec(open('setup_test_data.py').read())
"""

from academics.models import *
from django.contrib.auth import get_user_model

User = get_user_model()

print("🚀 Starting test data creation...\n")

# ============================================
# 1. CREATE USERS FOR ALL ROLES
# ============================================
print("📝 Creating users...")

users_data = [
    # STUDENTS
    {
        'username': 'student1',
        'email': 'student1@rci.edu',
        'password': 'test123',
        'role': 'student',
        'first_name': 'Juan',
        'last_name': 'Dela Cruz'
    },
    {
        'username': 'student2',
        'email': 'student2@rci.edu',
        'password': 'test123',
        'role': 'student',
        'first_name': 'Maria',
        'last_name': 'Santos'
    },
    {
        'username': 'student3',
        'email': 'student3@rci.edu',
        'password': 'test123',
        'role': 'student',
        'first_name': 'Pedro',
        'last_name': 'Reyes'
    },
    {
        'username': 'student4',
        'email': 'student4@rci.edu',
        'password': 'test123',
        'role': 'student',
        'first_name': 'Ana',
        'last_name': 'Garcia'
    },
    {
        'username': 'student5',
        'email': 'student5@rci.edu',
        'password': 'test123',
        'role': 'student',
        'first_name': 'Carlos',
        'last_name': 'Martinez'
    },
    
    # PROFESSORS
    {
        'username': 'prof1',
        'email': 'prof1@rci.edu',
        'password': 'test123',
        'role': 'professor',
        'first_name': 'Dr. Roberto',
        'last_name': 'Fernandez'
    },
    {
        'username': 'prof2',
        'email': 'prof2@rci.edu',
        'password': 'test123',
        'role': 'professor',
        'first_name': 'Prof. Linda',
        'last_name': 'Torres'
    },
    {
        'username': 'prof3',
        'email': 'prof3@rci.edu',
        'password': 'test123',
        'role': 'professor',
        'first_name': 'Dr. Miguel',
        'last_name': 'Navarro'
    },
    
    # REGISTRAR
    {
        'username': 'registrar1',
        'email': 'registrar@rci.edu',
        'password': 'test123',
        'role': 'registrar',
        'first_name': 'Grace',
        'last_name': 'Alvarez'
    },
    
    # ADMISSION
    {
        'username': 'admission1',
        'email': 'admission@rci.edu',
        'password': 'test123',
        'role': 'admissions',
        'first_name': 'Patricia',
        'last_name': 'Castillo'
    },
    
    # HEAD (Department Head)
    {
        'username': 'head1',
        'email': 'head@rci.edu',
        'password': 'test123',
        'role': 'head',
        'first_name': 'Dr. Ricardo',
        'last_name': 'Mendoza'
    },
    
    # ADMIN
    {
        'username': 'admin',
        'email': 'admin@rci.edu',
        'password': 'admin123',
        'role': 'admin',
        'first_name': 'System',
        'last_name': 'Administrator',
        'is_staff': True,
        'is_superuser': True
    },
]

created_users = {}
for user_data in users_data:
    username = user_data['username']
    if User.objects.filter(username=username).exists():
        user = User.objects.get(username=username)
        print(f"  ⚠️  User '{username}' already exists, skipping...")
    else:
        user = User.objects.create_user(**user_data)
        print(f"  ✅ Created user: {username} ({user_data['role']})")
    created_users[username] = user

print(f"\n✅ Users created: {len(created_users)}\n")


# ============================================
# 2. CREATE PROGRAMS
# ============================================
print("🎓 Creating programs...")

programs_data = [
    {
        'program_code': 'BSIT',
        'program_name': 'Bachelor of Science in Information Technology',
        'department': 'College of Computer Studies',
        'sector': 'Technology'
    },
    {
        'program_code': 'BSCS',
        'program_name': 'Bachelor of Science in Computer Science',
        'department': 'College of Computer Studies',
        'sector': 'Technology'
    },
    {
        'program_code': 'BSBA',
        'program_name': 'Bachelor of Science in Business Administration',
        'department': 'College of Business',
        'sector': 'Business'
    },
    {
        'program_code': 'BSA',
        'program_name': 'Bachelor of Science in Accountancy',
        'department': 'College of Business',
        'sector': 'Business'
    },
    {
        'program_code': 'BSED',
        'program_name': 'Bachelor of Secondary Education',
        'department': 'College of Education',
        'sector': 'Education'
    },
]

programs = {}
for prog_data in programs_data:
    prog, created = Program.objects.get_or_create(
        program_code=prog_data['program_code'],
        defaults=prog_data
    )
    programs[prog_data['program_code']] = prog
    status = "Created" if created else "Exists"
    print(f"  {status}: {prog_data['program_code']} - {prog_data['program_name']}")

print(f"\n✅ Programs ready: {len(programs)}\n")


# ============================================
# 3. CREATE CURRICULUMS
# ============================================
print("📚 Creating curriculums...")

curriculums = {}
for program_code, program in programs.items():
    for year in range(1, 5):  # Years 1-4
        for semester in ['1st', '2nd']:
            curr, created = Curriculum.objects.get_or_create(
                program=program,
                year_level=year,
                semester=semester
            )
            curriculums[f"{program_code}-{year}-{semester}"] = curr
            if created:
                print(f"  ✅ Created: {program_code} Year {year} {semester} Semester")

print(f"\n✅ Curriculums created: {len(curriculums)}\n")


# ============================================
# 4. CREATE SUBJECTS
# ============================================
print("📖 Creating subjects...")

subjects_data = [
    # BSIT Year 3, 1st Semester
    ('IT301', 'Web Development Fundamentals', 3, 'BSIT-3-1st', 'Learn HTML, CSS, and JavaScript basics'),
    ('IT302', 'Database Management Systems', 3, 'BSIT-3-1st', 'Relational databases and SQL'),
    ('IT303', 'Data Structures and Algorithms', 3, 'BSIT-3-1st', 'Advanced data structures'),
    ('IT304', 'Object-Oriented Programming', 3, 'BSIT-3-1st', 'OOP concepts and design patterns'),
    ('IT305', 'Systems Analysis and Design', 3, 'BSIT-3-1st', 'Software development lifecycle'),
    
    # BSIT Year 3, 2nd Semester
    ('IT306', 'Web Development Advanced', 3, 'BSIT-3-2nd', 'React, Node.js, and modern frameworks'),
    ('IT307', 'Mobile Application Development', 3, 'BSIT-3-2nd', 'iOS and Android development'),
    ('IT308', 'Network Administration', 3, 'BSIT-3-2nd', 'Network protocols and security'),
    ('IT309', 'Information Security', 3, 'BSIT-3-2nd', 'Cybersecurity fundamentals'),
    ('IT310', 'Software Engineering', 3, 'BSIT-3-2nd', 'Software project management'),
    
    # BSCS Year 3, 1st Semester
    ('CS301', 'Algorithm Analysis', 3, 'BSCS-3-1st', 'Computational complexity'),
    ('CS302', 'Computer Architecture', 3, 'BSCS-3-1st', 'Hardware and low-level programming'),
    ('CS303', 'Operating Systems', 3, 'BSCS-3-1st', 'OS concepts and design'),
    ('CS304', 'Artificial Intelligence', 3, 'BSCS-3-1st', 'AI and machine learning basics'),
    ('CS305', 'Database Theory', 3, 'BSCS-3-1st', 'Advanced database concepts'),
    
    # BSBA Year 2, 1st Semester
    ('BA201', 'Financial Management', 3, 'BSBA-2-1st', 'Corporate finance principles'),
    ('BA202', 'Marketing Management', 3, 'BSBA-2-1st', 'Marketing strategies'),
    ('BA203', 'Human Resource Management', 3, 'BSBA-2-1st', 'HR policies and practices'),
]

subjects = {}
for code, title, units, curr_key, summary in subjects_data:
    curriculum = curriculums.get(curr_key)
    if curriculum:
        subj, created = Subject.objects.get_or_create(
            code=code,
            defaults={
                'title': title,
                'units': units,
                'curriculum': curriculum,
                'summary': summary
            }
        )
        subjects[code] = subj
        status = "Created" if created else "Exists"
        print(f"  {status}: {code} - {title}")

print(f"\n✅ Subjects created: {len(subjects)}\n")


# ============================================
# 5. CREATE SECTIONS
# ============================================
print("🏫 Creating sections...")

sections_data = [
    # IT301 - Web Development (Prof 1)
    ('IT301-A', 'IT301', '2024-2025-1st', 'MWF 8:00-9:30 AM', 'IT-Lab1', 'prof1'),
    ('IT301-B', 'IT301', '2024-2025-1st', 'MWF 10:00-11:30 AM', 'IT-Lab1', 'prof1'),
    
    # IT302 - Database (Prof 2)
    ('IT302-A', 'IT302', '2024-2025-1st', 'TTH 8:00-9:30 AM', 'IT-Lab2', 'prof2'),
    ('IT302-B', 'IT302', '2024-2025-1st', 'TTH 1:00-2:30 PM', 'IT-Lab2', 'prof2'),
    
    # IT303 - Data Structures (Prof 3)
    ('IT303-A', 'IT303', '2024-2025-1st', 'MWF 1:00-2:30 PM', 'IT-Lab3', 'prof3'),
    
    # IT304 - OOP (Prof 1)
    ('IT304-A', 'IT304', '2024-2025-1st', 'TTH 10:00-11:30 AM', 'IT-Lab1', 'prof1'),
    
    # IT305 - Systems Analysis (Prof 2)
    ('IT305-A', 'IT305', '2024-2025-1st', 'MWF 3:00-4:30 PM', 'IT-Lab2', 'prof2'),
    
    # CS subjects
    ('CS301-A', 'CS301', '2024-2025-1st', 'MWF 9:00-10:30 AM', 'CS-Lab1', 'prof3'),
    ('CS302-A', 'CS302', '2024-2025-1st', 'TTH 9:00-10:30 AM', 'CS-Lab1', 'prof1'),
    
    # Business subjects
    ('BA201-A', 'BA201', '2024-2025-1st', 'MWF 8:00-9:30 AM', 'BUS-101', 'prof2'),
    ('BA202-A', 'BA202', '2024-2025-1st', 'TTH 8:00-9:30 AM', 'BUS-102', 'prof3'),
]

sections = {}
for section_name, subject_code, term, schedule, room, prof_username in sections_data:
    subject = subjects.get(subject_code)
    professor = created_users.get(prof_username)
    
    if subject and professor:
        sect, created = Section.objects.get_or_create(
            section_name=section_name,
            term=term,
            defaults={
                'subject': subject,
                'schedule': schedule,
                'room': room,
                'professor': professor
            }
        )
        sections[section_name] = sect
        status = "Created" if created else "Exists"
        print(f"  {status}: {section_name} - {subject.code} ({schedule})")

print(f"\n✅ Sections created: {len(sections)}\n")


# ============================================
# 6. CREATE STUDENT PROFILES
# ============================================
print("👨‍🎓 Creating student profiles...")

students_data = [
    ('student1', '2021-00001', 'BSIT', 3, 'enrolled'),
    ('student2', '2021-00002', 'BSIT', 3, 'enrolled'),
    ('student3', '2021-00003', 'BSCS', 3, 'enrolled'),
    ('student4', '2022-00001', 'BSBA', 2, 'enrolled'),
    ('student5', '2023-00001', 'BSIT', 1, 'enrolled'),
]

students = {}
for username, student_number, program_code, year_level, status in students_data:
    user = created_users.get(username)
    program = programs.get(program_code)
    
    if user and program:
        stud, created = Student.objects.get_or_create(
            user=user,
            defaults={
                'student_number': student_number,
                'program': program,
                'year_level': year_level,
                'status': status
            }
        )
        students[username] = stud
        status_text = "Created" if created else "Exists"
        print(f"  {status_text}: {student_number} - {user.get_full_name()} ({program_code})")

print(f"\n✅ Student profiles created: {len(students)}\n")


# ============================================
# 7. CREATE ENROLLMENTS
# ============================================
print("📝 Creating enrollments...")

enrollments_data = [
    # student1 - Full load (5 subjects)
    ('student1', 'IT301-A', '2024-2025-1st', 'enrolled'),
    ('student1', 'IT302-A', '2024-2025-1st', 'enrolled'),
    ('student1', 'IT303-A', '2024-2025-1st', 'enrolled'),
    ('student1', 'IT304-A', '2024-2025-1st', 'enrolled'),
    ('student1', 'IT305-A', '2024-2025-1st', 'pending'),
    
    # student2 - Medium load (4 subjects)
    ('student2', 'IT301-B', '2024-2025-1st', 'enrolled'),
    ('student2', 'IT302-B', '2024-2025-1st', 'enrolled'),
    ('student2', 'IT303-A', '2024-2025-1st', 'enrolled'),
    ('student2', 'IT304-A', '2024-2025-1st', 'pending'),
    
    # student3 - CS student (3 subjects)
    ('student3', 'CS301-A', '2024-2025-1st', 'enrolled'),
    ('student3', 'CS302-A', '2024-2025-1st', 'enrolled'),
    ('student3', 'IT302-A', '2024-2025-1st', 'enrolled'),
    
    # student4 - Business student (2 subjects)
    ('student4', 'BA201-A', '2024-2025-1st', 'enrolled'),
    ('student4', 'BA202-A', '2024-2025-1st', 'enrolled'),
    
    # student5 - Light load (2 subjects)
    ('student5', 'IT301-A', '2024-2025-1st', 'enrolled'),
    ('student5', 'IT302-A', '2024-2025-1st', 'pending'),
]

enrollment_count = 0
for username, section_name, term, status in enrollments_data:
    student = students.get(username)
    section = sections.get(section_name)
    
    if student and section:
        enroll, created = Enrollment.objects.get_or_create(
            student=student,
            section=section,
            term=term,
            defaults={'status': status}
        )
        if created:
            enrollment_count += 1
            print(f"  ✅ {student.student_number} enrolled in {section_name} ({status})")

print(f"\n✅ Enrollments created: {enrollment_count}\n")


# ============================================
# 8. CREATE SAMPLE GRADES
# ============================================
print("📊 Creating sample grades...")

grades_data = [
    # student1 - Previous semester grades
    ('student1', 'IT301', 'IT301-A', 1.75, 'passed', 'prof1'),
    ('student1', 'IT302', 'IT302-A', 2.00, 'passed', 'prof2'),
    ('student1', 'IT303', 'IT303-A', 1.50, 'passed', 'prof3'),
    
    # student2 - Mixed grades
    ('student2', 'IT301', 'IT301-B', 2.25, 'passed', 'prof1'),
    ('student2', 'IT302', 'IT302-B', 1.75, 'passed', 'prof2'),
    ('student2', 'IT304', 'IT304-A', None, 'inc', 'prof1'),  # INC
    
    # student3
    ('student3', 'CS301', 'CS301-A', 1.25, 'passed', 'prof3'),
    ('student3', 'CS302', 'CS302-A', 1.50, 'passed', 'prof1'),
]

grade_count = 0
for username, subject_code, section_name, grade, status, prof_username in grades_data:
    student = students.get(username)
    subject = subjects.get(subject_code)
    section = sections.get(section_name)
    encoded_by = created_users.get(prof_username)
    
    if student and subject and section and encoded_by:
        grade_obj, created = Grade.objects.get_or_create(
            student=student,
            subject=subject,
            section=section,
            defaults={
                'grade': grade,
                'status': status,
                'encoded_by': encoded_by
            }
        )
        if created:
            grade_count += 1
            grade_str = f"{grade:.2f}" if grade else "INC"
            print(f"  ✅ {student.student_number} - {subject_code}: {grade_str} ({status})")

print(f"\n✅ Grades created: {grade_count}\n")


# ============================================
# 9. CREATE SAMPLE APPLICATIONS
# ============================================
print("📄 Creating sample applications...")

applications_data = [
    ('Jose Rizal', 'jose.rizal@email.com', 'BSIT', 'pending'),
    ('Andres Bonifacio', 'andres.bonifacio@email.com', 'BSCS', 'pending'),
    ('Emilio Aguinaldo', 'emilio.aguinaldo@email.com', 'BSBA', 'accepted'),
    ('Apolinario Mabini', 'apolinario.mabini@email.com', 'BSA', 'rejected'),
]

app_count = 0
for name, email, program_code, status in applications_data:
    program = programs.get(program_code)
    if program:
        app, created = Application.objects.get_or_create(
            email=email,
            defaults={
                'applicant_name': name,
                'program': program,
                'status': status,
                'uploaded_requirements': ['Form137.pdf', 'BirthCertificate.pdf']
            }
        )
        if created:
            app_count += 1
            print(f"  ✅ {name} - {program_code} ({status})")

print(f"\n✅ Applications created: {app_count}\n")


# ============================================
# 10. SUMMARY
# ============================================
print("\n" + "="*50)
print("🎉 TEST DATA CREATION COMPLETE!")
print("="*50)
print(f"""
📊 Summary:
  • Users: {User.objects.count()}
  • Programs: {Program.objects.count()}
  • Curriculums: {Curriculum.objects.count()}
  • Subjects: {Subject.objects.count()}
  • Sections: {Section.objects.count()}
  • Students: {Student.objects.count()}
  • Enrollments: {Enrollment.objects.count()}
  • Grades: {Grade.objects.count()}
  • Applications: {Application.objects.count()}

🔐 Test User Credentials:
  ┌─────────────┬──────────────┬────────────┐
  │ Username    │ Password     │ Role       │
  ├─────────────┼──────────────┼────────────┤
  │ student1    │ test123      │ Student    │
  │ student2    │ test123      │ Student    │
  │ student3    │ test123      │ Student    │
  │ student4    │ test123      │ Student    │
  │ student5    │ test123      │ Student    │
  │ prof1       │ test123      │ Professor  │
  │ prof2       │ test123      │ Professor  │
  │ prof3       │ test123      │ Professor  │
  │ registrar1  │ test123      │ Registrar  │
  │ admission1  │ test123      │ Admission  │
  │ head1       │ test123      │ Head       │
  │ admin       │ admin123     │ Admin      │
  └─────────────┴──────────────┴────────────┘

✅ You can now login with any of these accounts!
""")

print("\n💡 Quick Test Commands:")
print("  • Login as student: username='student1', password='test123'")
print("  • Login as professor: username='prof1', password='test123'")
print("  • Login as registrar: username='registrar1', password='test123'")
print("  • Login as admin: username='admin', password='admin123'")
print("\n✨ Happy testing!\n")