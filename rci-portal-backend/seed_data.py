import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rci_portal.settings')
django.setup()

from academics.models import (
    User, Program, Curriculum, Subject, Section,
    Student, Enrollment, Grade
)
from django.db import transaction

PRINT_PASSWORD = "password123"

print("🌱 Starting database seeding...\n")

# ========================================
# 1. CREATE PROGRAMS
# ========================================
print("📚 Creating Programs...")

programs_data = [
    # 4-YEAR PROGRAMS
    {'code': 'BSTM', 'name': 'Bachelor of Science in Tourism Management', 'department': 'Tourism & Hospitality', 'sector': 'Tourism', 'years': 4},
    {'code': 'BSIS', 'name': 'Bachelor of Science in Information Systems', 'department': 'ICTD', 'sector': 'IT', 'years': 4},
    {'code': 'BSAIS', 'name': 'Bachelor of Science in Accounting Information Systems', 'department': 'Business', 'sector': 'Business', 'years': 4},
    {'code': 'BSCRIM', 'name': 'Bachelor of Science in Criminology', 'department': 'Criminology', 'sector': 'Law Enforcement', 'years': 4},
    {'code': 'BCED', 'name': 'Bachelor of Culture and Arts Education', 'department': 'Education', 'sector': 'Education', 'years': 4},
    {'code': 'BTVTED', 'name': 'Bachelor of Technical-Vocational Teacher Education', 'department': 'Education', 'sector': 'Education', 'years': 4},
    {'code': 'BSN', 'name': 'Bachelor of Science in Nursing', 'department': 'Nursing', 'sector': 'Healthcare', 'years': 4},
    {'code': 'BSEntrep', 'name': 'Bachelor of Science in Entrepreneurship', 'department': 'Business', 'sector': 'Business', 'years': 4},
    {'code': 'BSCE', 'name': 'Bachelor of Science in Civil Engineering', 'department': 'Engineering', 'sector': 'Engineering', 'years': 4},

    # 3-YEAR PROGRAMS
    {'code': 'TTHMT', 'name': 'Tourism and Hospitality Management Technology', 'department': 'Tourism & Hospitality', 'sector': 'Tourism', 'years': 3},
    {'code': 'BFDIS', 'name': 'Business and Financial Data Information System', 'department': 'Business', 'sector': 'IT/Business', 'years': 3},

    # 2-YEAR PROGRAMS
    {'code': 'HRS', 'name': 'Hospitality and Restaurant Services', 'department': 'Tourism & Hospitality', 'sector': 'Hospitality', 'years': 2},
    {'code': 'CRS', 'name': 'Culinary and Restaurant Services', 'department': 'Tourism & Hospitality', 'sector': 'Culinary', 'years': 2},
    {'code': 'BOAT', 'name': 'Business Office and Accounting Technology', 'department': 'Business', 'sector': 'Business', 'years': 2},
    {'code': 'SSWT', 'name': 'Salon, Spa and Wellness Technology', 'department': 'Wellness', 'sector': 'Wellness', 'years': 2},
    {'code': 'ICT', 'name': 'Information and Communication Technology', 'department': 'ICTD', 'sector': 'IT', 'years': 2},
]

programs = {}
for data in programs_data:
    program, created = Program.objects.get_or_create(
        program_code=data['code'],
        defaults={
            'program_name': data['name'],
            'department': data['department'],
            'sector': data['sector']
        }
    )
    programs[data['code']] = program
    status = "✅ Created" if created else "⏭️  Exists"
    print(f"  {status}: {data['code']} - {data['name']}")

print(f"\n✅ Total Programs: {len(programs)}\n")

# ========================================
# 2. CREATE USERS
# ========================================
print("👥 Creating Users...")

users_data = [
    # Admin (full superuser)
    {
        'username': 'admin',
        'email': 'admin@rci.edu',
        'role': 'admin',
        'first_name': 'System',
        'last_name': 'Admin',
        'is_staff': True,
        'is_superuser': True
    },

    # Registrars (staff, but not superuser)
    {
        'username': 'registrar1',
        'email': 'registrar@rci.edu',
        'role': 'registrar',
        'first_name': 'Maria',
        'last_name': 'Santos',
        'is_staff': True,
        'is_superuser': False
    },

    # Admission Officers (staff)
    {
        'username': 'admission1',
        'email': 'admission@rci.edu',
        'role': 'admission',
        'first_name': 'Juan',
        'last_name': 'Cruz',
        'is_staff': True,
        'is_superuser': False
    },

    # Department Heads (staff)
    {
        'username': 'head_ictd',
        'email': 'head.ictd@rci.edu',
        'role': 'head',
        'first_name': 'Robert',
        'last_name': 'Garcia',
        'is_staff': True,
        'is_superuser': False
    },
    {
        'username': 'head_business',
        'email': 'head.business@rci.edu',
        'role': 'head',
        'first_name': 'Ana',
        'last_name': 'Reyes',
        'is_staff': True,
        'is_superuser': False
    },

    # Professors
    {'username': 'prof_dela_cruz', 'email': 'jdelacruz@rci.edu', 'role': 'professor', 'first_name': 'Jose', 'last_name': 'Dela Cruz'},
    {'username': 'prof_santos', 'email': 'msantos@rci.edu', 'role': 'professor', 'first_name': 'Maria', 'last_name': 'Santos'},
    {'username': 'prof_reyes', 'email': 'areyes@rci.edu', 'role': 'professor', 'first_name': 'Antonio', 'last_name': 'Reyes'},
    {'username': 'prof_garcia', 'email': 'lgarcia@rci.edu', 'role': 'professor', 'first_name': 'Linda', 'last_name': 'Garcia'},
    {'username': 'prof_cenita', 'email': 'ajcenita@rci.edu', 'role': 'professor', 'first_name': 'Angelo Jonelle', 'last_name': 'Cenita'},
    {'username': 'prof_africa', 'email': 'fiafrica@rci.edu', 'role': 'professor', 'first_name': 'Francis Ian', 'last_name': 'Africa'},
    {'username': 'prof_delmonte', 'email': 'vdelmonte@rci.edu', 'role': 'professor', 'first_name': 'Vergil', 'last_name': 'Del Monte'},
    {'username': 'prof_orendain', 'email': 'aorendain@rci.edu', 'role': 'professor', 'first_name': 'Angel', 'last_name': 'Orendain'},
    {'username': 'prof_pangilinan', 'email': 'apangilinan@rci.edu', 'role': 'professor', 'first_name': 'Arianne', 'last_name': 'Pangilinan'},

    # Students
        # Students
    {'username': 'student_kirt', 'email': 'kirt@student.rci.edu', 'role': 'student', 'first_name': 'Kirt', 'last_name': 'Backend'},
    {'username': 'student_jun', 'email': 'jun@student.rci.edu', 'role': 'student', 'first_name': 'Jun', 'last_name': 'Manager'},
    {'username': 'student_anna', 'email': 'anna@student.rci.edu', 'role': 'student', 'first_name': 'Anna', 'last_name': 'Cruz'},
    {'username': 'student_pedro', 'email': 'pedro@student.rci.edu', 'role': 'student', 'first_name': 'Pedro', 'last_name': 'Santos'},
    {'username': 'student_lisa', 'email': 'lisa@student.rci.edu', 'role': 'student', 'first_name': 'Lisa', 'last_name': 'Reyes'},
    {'username': 'student_rafael', 'email': 'rafael@student.rci.edu', 'role': 'student', 'first_name': 'Rafael', 'last_name': 'Domingo'},
    {'username': 'student_joyce', 'email': 'joyce@student.rci.edu', 'role': 'student', 'first_name': 'Joyce', 'last_name': 'Delos Santos'},
    {'username': 'student_ian', 'email': 'ian@student.rci.edu', 'role': 'student', 'first_name': 'Ian', 'last_name': 'Garcia'},
    {'username': 'student_marie', 'email': 'marie@student.rci.edu', 'role': 'student', 'first_name': 'Marie', 'last_name': 'Tan'},
    {'username': 'student_kyle', 'email': 'kyle@student.rci.edu', 'role': 'student', 'first_name': 'Kyle', 'last_name': 'Valdez'},
    {'username': 'student_sophia', 'email': 'sophia@student.rci.edu', 'role': 'student', 'first_name': 'Sophia', 'last_name': 'Lopez'},
    {'username': 'student_josh', 'email': 'josh@student.rci.edu', 'role': 'student', 'first_name': 'Josh', 'last_name': 'Aquino'},
    {'username': 'student_megan', 'email': 'megan@student.rci.edu', 'role': 'student', 'first_name': 'Megan', 'last_name': 'Ramos'},
    {'username': 'student_matt', 'email': 'matt@student.rci.edu', 'role': 'student', 'first_name': 'Matt', 'last_name': 'Chavez'},
    {'username': 'student_ella', 'email': 'ella@student.rci.edu', 'role': 'student', 'first_name': 'Ella', 'last_name': 'Torres'},
    {'username': 'student_jason', 'email': 'jason@student.rci.edu', 'role': 'student', 'first_name': 'Jason', 'last_name': 'Lim'},
    {'username': 'student_grace', 'email': 'grace@student.rci.edu', 'role': 'student', 'first_name': 'Grace', 'last_name': 'Fernandez'},
    {'username': 'student_carlo', 'email': 'carlo@student.rci.edu', 'role': 'student', 'first_name': 'Carlo', 'last_name': 'Dela Cruz'},
    {'username': 'student_nina', 'email': 'nina@student.rci.edu', 'role': 'student', 'first_name': 'Nina', 'last_name': 'Bautista'},
    {'username': 'student_paul', 'email': 'paul@student.rci.edu', 'role': 'student', 'first_name': 'Paul', 'last_name': 'Mendoza'},

]

users = {}
for data in users_data:
    # create or fetch
    user, created = User.objects.get_or_create(
        username=data['username'],
        defaults={
            'email': data.get('email', ''),
            'role': data.get('role', ''),
            'first_name': data.get('first_name', ''),
            'last_name': data.get('last_name', ''),
        }
    )

    if created:
        user.set_password(PRINT_PASSWORD)
        user.is_staff = data.get('is_staff', False)
        user.is_superuser = data.get('is_superuser', False)
        user.save()
        status = "✅ Created"
    else:
        changed = False
        if data.get('is_staff', False) and not user.is_staff:
            user.is_staff = True
            changed = True
        if data.get('is_superuser', False) and not user.is_superuser:
            user.is_superuser = True
            changed = True
        user.set_password(PRINT_PASSWORD)
        changed = True
        if changed:
            user.save()
        status = "⏭️  Exists (updated)" if changed else "⏭️  Exists"

    users[data['username']] = user
    print(f"  {status}: {data['username']} ({data.get('role','')}) - {data.get('first_name','')} {data.get('last_name','')}")

print(f"\n✅ Total Users: {len(users)}")
print(f"🔑 Default password for all users (dev): {PRINT_PASSWORD}\n")

# ========================================
# 3. STUDENT PROFILES
# ========================================
print("🎓 Creating Student Profiles...")

students_data = [
    {'username': 'student_kirt', 'student_number': '2021-00001', 'program': 'BSIS', 'year_level': 3, 'status': 'enrolled'},
    {'username': 'student_jun', 'student_number': '2021-00002', 'program': 'BSIS', 'year_level': 3, 'status': 'enrolled'},
    {'username': 'student_anna', 'student_number': '2022-00003', 'program': 'BSAIS', 'year_level': 2, 'status': 'enrolled'},
    {'username': 'student_pedro', 'student_number': '2023-00004', 'program': 'ICT', 'year_level': 1, 'status': 'enrolled'},
    {'username': 'student_lisa', 'student_number': '2022-00005', 'program': 'BSTM', 'year_level': 2, 'status': 'enrolled'},
    {'username': 'student_rafael', 'student_number': '2023-00006', 'program': 'BSCRIM', 'year_level': 1, 'status': 'enrolled'},
    {'username': 'student_joyce', 'student_number': '2022-00007', 'program': 'BSAIS', 'year_level': 2, 'status': 'enrolled'},
    {'username': 'student_ian', 'student_number': '2021-00008', 'program': 'BSTM', 'year_level': 4, 'status': 'enrolled'},
    {'username': 'student_marie', 'student_number': '2021-00009', 'program': 'BSN', 'year_level': 4, 'status': 'enrolled'},
    {'username': 'student_kyle', 'student_number': '2023-00010', 'program': 'BSIS', 'year_level': 1, 'status': 'enrolled'},
    {'username': 'student_sophia', 'student_number': '2022-00011', 'program': 'BSAIS', 'year_level': 2, 'status': 'enrolled'},
    {'username': 'student_josh', 'student_number': '2021-00012', 'program': 'ICT', 'year_level': 3, 'status': 'enrolled'},
    {'username': 'student_megan', 'student_number': '2022-00013', 'program': 'BSCRIM', 'year_level': 2, 'status': 'enrolled'},
    {'username': 'student_matt', 'student_number': '2023-00014', 'program': 'BSIS', 'year_level': 1, 'status': 'enrolled'},
    {'username': 'student_ella', 'student_number': '2022-00015', 'program': 'BSTM', 'year_level': 2, 'status': 'enrolled'},
    {'username': 'student_jason', 'student_number': '2023-00016', 'program': 'BSN', 'year_level': 1, 'status': 'enrolled'},
    {'username': 'student_grace', 'student_number': '2021-00017', 'program': 'BSCRIM', 'year_level': 4, 'status': 'enrolled'},
    {'username': 'student_carlo', 'student_number': '2022-00018', 'program': 'BSIS', 'year_level': 2, 'status': 'enrolled'},
    {'username': 'student_nina', 'student_number': '2023-00019', 'program': 'BSTM', 'year_level': 1, 'status': 'enrolled'},
    {'username': 'student_paul', 'student_number': '2021-00020', 'program': 'BSAIS', 'year_level': 4, 'status': 'enrolled'},
]


students = {}
for data in students_data:
    user = users.get(data['username'])
    if not user:
        print(f"  ⚠️  Skipping student creation: user {data['username']} not found")
        continue

    student, created = Student.objects.get_or_create(
        student_number=data['student_number'],  # ✅ lookup by student_number
        defaults={
            'user': user,
            'program': programs[data['program']],
            'year_level': data['year_level'],
            'status': data['status'],
        }
    )

    # ✅ Optional: ensure user and other fields are updated if the student already exists
    if not created:
        student.user = user
        student.program = programs[data['program']]
        student.year_level = data['year_level']
        student.status = data['status']
        student.save()

    students[data['student_number']] = student
    status = "✅ Created" if created else "⏭️  Exists"
    print(f"  {status}: {data['student_number']} - {user.get_full_name()} ({data['program']})")

print(f"\n✅ Total Students: {len(students)}\n")


# ============================
# 4. CURRICULUMS BY PROGRAM
# ============================

print("📋 Creating Sample Curriculum for all programs...")

# ========================================
# 4-YEAR PROGRAMS
# ========================================

# 🧩 BSTM - Bachelor of Science in Tourism Management
bstm_program = programs['BSTM']
bstm_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=1, semester='1st')
bstm_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=1, semester='2nd')
bstm_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=2, semester='1st')
bstm_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=2, semester='2nd')
bstm_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=3, semester='1st')
bstm_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=3, semester='2nd')
bstm_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=4, semester='1st')
bstm_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bstm_program, year_level=4, semester='2nd')

# 🧩 BSIS - Bachelor of Science in Information Systems
bsis_program = programs['BSIS']
bsis_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=1, semester='1st')
bsis_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=1, semester='2nd')
bsis_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=2, semester='1st')
bsis_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=2, semester='2nd')
bsis_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=3, semester='1st')
bsis_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=3, semester='2nd')
bsis_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=4, semester='1st')
bsis_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bsis_program, year_level=4, semester='2nd')

# 🧩 BSAIS - Bachelor of Science in Accounting Information Systems
bsais_program = programs['BSAIS']
bsais_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=1, semester='1st')
bsais_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=1, semester='2nd')
bsais_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=2, semester='1st')
bsais_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=2, semester='2nd')
bsais_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=3, semester='1st')
bsais_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=3, semester='2nd')
bsais_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=4, semester='1st')
bsais_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bsais_program, year_level=4, semester='2nd')

# 🧩 BSCRIM - Bachelor of Science in Criminology
bscrim_program = programs['BSCRIM']
bscrim_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=1, semester='1st')
bscrim_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=1, semester='2nd')
bscrim_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=2, semester='1st')
bscrim_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=2, semester='2nd')
bscrim_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=3, semester='1st')
bscrim_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=3, semester='2nd')
bscrim_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=4, semester='1st')
bscrim_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bscrim_program, year_level=4, semester='2nd')

# 🧩 BCED - Bachelor of Culture and Arts Education
bced_program = programs['BCED']
bced_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bced_program, year_level=1, semester='1st')
bced_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bced_program, year_level=1, semester='2nd')
bced_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bced_program, year_level=2, semester='1st')
bced_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bced_program, year_level=2, semester='2nd')
bced_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bced_program, year_level=3, semester='1st')
bced_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bced_program, year_level=3, semester='2nd')
bced_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bced_program, year_level=4, semester='1st')
bced_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bced_program, year_level=4, semester='2nd')

# 🧩 BTVTED - Bachelor of Technical-Vocational Teacher Education
btvted_program = programs['BTVTED']
btvted_curriculum_1_1, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=1, semester='1st')
btvted_curriculum_1_2, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=1, semester='2nd')
btvted_curriculum_2_1, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=2, semester='1st')
btvted_curriculum_2_2, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=2, semester='2nd')
btvted_curriculum_3_1, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=3, semester='1st')
btvted_curriculum_3_2, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=3, semester='2nd')
btvted_curriculum_4_1, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=4, semester='1st')
btvted_curriculum_4_2, created = Curriculum.objects.get_or_create(program=btvted_program, year_level=4, semester='2nd')

# 🧩 BSN - Bachelor of Science in Nursing
bsn_program = programs['BSN']
bsn_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=1, semester='1st')
bsn_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=1, semester='2nd')
bsn_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=2, semester='1st')
bsn_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=2, semester='2nd')
bsn_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=3, semester='1st')
bsn_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=3, semester='2nd')
bsn_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=4, semester='1st')
bsn_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bsn_program, year_level=4, semester='2nd')

# 🧩 BSEntrep - Bachelor of Science in Entrepreneurship
bsentrep_program = programs['BSEntrep']
bsentrep_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=1, semester='1st')
bsentrep_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=1, semester='2nd')
bsentrep_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=2, semester='1st')
bsentrep_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=2, semester='2nd')
bsentrep_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=3, semester='1st')
bsentrep_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=3, semester='2nd')
bsentrep_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=4, semester='1st')
bsentrep_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bsentrep_program, year_level=4, semester='2nd')

# 🧩 BSCE - Bachelor of Science in Civil Engineering
bsce_program = programs['BSCE']
bsce_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=1, semester='1st')
bsce_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=1, semester='2nd')
bsce_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=2, semester='1st')
bsce_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=2, semester='2nd')
bsce_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=3, semester='1st')
bsce_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=3, semester='2nd')
bsce_curriculum_4_1, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=4, semester='1st')
bsce_curriculum_4_2, created = Curriculum.objects.get_or_create(program=bsce_program, year_level=4, semester='2nd')

# ========================================
# 3-YEAR PROGRAMS
# ========================================

# 🧩 TTHMT - Tourism and Hospitality Management Technology
tthmt_program = programs['TTHMT']
tthmt_curriculum_1_1, created = Curriculum.objects.get_or_create(program=tthmt_program, year_level=1, semester='1st')
tthmt_curriculum_1_2, created = Curriculum.objects.get_or_create(program=tthmt_program, year_level=1, semester='2nd')
tthmt_curriculum_2_1, created = Curriculum.objects.get_or_create(program=tthmt_program, year_level=2, semester='1st')
tthmt_curriculum_2_2, created = Curriculum.objects.get_or_create(program=tthmt_program, year_level=2, semester='2nd')
tthmt_curriculum_3_1, created = Curriculum.objects.get_or_create(program=tthmt_program, year_level=3, semester='1st')
tthmt_curriculum_3_2, created = Curriculum.objects.get_or_create(program=tthmt_program, year_level=3, semester='2nd')

# 🧩 BFDIS - Business and Financial Data Information System
bfdis_program = programs['BFDIS']
bfdis_curriculum_1_1, created = Curriculum.objects.get_or_create(program=bfdis_program, year_level=1, semester='1st')
bfdis_curriculum_1_2, created = Curriculum.objects.get_or_create(program=bfdis_program, year_level=1, semester='2nd')
bfdis_curriculum_2_1, created = Curriculum.objects.get_or_create(program=bfdis_program, year_level=2, semester='1st')
bfdis_curriculum_2_2, created = Curriculum.objects.get_or_create(program=bfdis_program, year_level=2, semester='2nd')
bfdis_curriculum_3_1, created = Curriculum.objects.get_or_create(program=bfdis_program, year_level=3, semester='1st')
bfdis_curriculum_3_2, created = Curriculum.objects.get_or_create(program=bfdis_program, year_level=3, semester='2nd')

# ========================================
# 2-YEAR PROGRAMS
# ========================================

# 🧩 HRS - Hospitality and Restaurant Services
hrs_program = programs['HRS']
hrs_curriculum_1_1, created = Curriculum.objects.get_or_create(program=hrs_program, year_level=1, semester='1st')
hrs_curriculum_1_2, created = Curriculum.objects.get_or_create(program=hrs_program, year_level=1, semester='2nd')
hrs_curriculum_2_1, created = Curriculum.objects.get_or_create(program=hrs_program, year_level=2, semester='1st')
hrs_curriculum_2_2, created = Curriculum.objects.get_or_create(program=hrs_program, year_level=2, semester='2nd')

# 🧩 CRS - Culinary and Restaurant Services
crs_program = programs['CRS']
crs_curriculum_1_1, created = Curriculum.objects.get_or_create(program=crs_program, year_level=1, semester='1st')
crs_curriculum_1_2, created = Curriculum.objects.get_or_create(program=crs_program, year_level=1, semester='2nd')
crs_curriculum_2_1, created = Curriculum.objects.get_or_create(program=crs_program, year_level=2, semester='1st')
crs_curriculum_2_2, created = Curriculum.objects.get_or_create(program=crs_program, year_level=2, semester='2nd')

# 🧩 BOAT - Business Office and Accounting Technology
boat_program = programs['BOAT']
boat_curriculum_1_1, created = Curriculum.objects.get_or_create(program=boat_program, year_level=1, semester='1st')
boat_curriculum_1_2, created = Curriculum.objects.get_or_create(program=boat_program, year_level=1, semester='2nd')
boat_curriculum_2_1, created = Curriculum.objects.get_or_create(program=boat_program, year_level=2, semester='1st')
boat_curriculum_2_2, created = Curriculum.objects.get_or_create(program=boat_program, year_level=2, semester='2nd')

# 🧩 SSWT - Salon, Spa and Wellness Technology
sswt_program = programs['SSWT']
sswt_curriculum_1_1, created = Curriculum.objects.get_or_create(program=sswt_program, year_level=1, semester='1st')
sswt_curriculum_1_2, created = Curriculum.objects.get_or_create(program=sswt_program, year_level=1, semester='2nd')
sswt_curriculum_2_1, created = Curriculum.objects.get_or_create(program=sswt_program, year_level=2, semester='1st')
sswt_curriculum_2_2, created = Curriculum.objects.get_or_create(program=sswt_program, year_level=2, semester='2nd')

# 🧩 ICT - Information and Communication Technology
ict_program = programs['ICT']
ict_curriculum_1_1, created = Curriculum.objects.get_or_create(program=ict_program, year_level=1, semester='1st')
ict_curriculum_1_2, created = Curriculum.objects.get_or_create(program=ict_program, year_level=1, semester='2nd')
ict_curriculum_2_1, created = Curriculum.objects.get_or_create(program=ict_program, year_level=2, semester='1st')
ict_curriculum_2_2, created = Curriculum.objects.get_or_create(program=ict_program, year_level=2, semester='2nd')

# ========================================
# 5. SAMPLE SUBJECTS
# ========================================
print("📖 Creating Sample Subjects...")

subjects_data = [

    # Information Technology (IT) - BSIS
    {'code': 'IS101-A', 'title': 'Introduction to Computing', 'units': 3, 'curriculum': bsis_curriculum_1_1, 'prerequisites': [], 'summary': 'Basic computing concepts and computer literacy'},
    {'code': 'IS101-B', 'title': 'Computer Programming 1', 'units': 3, 'curriculum': bsis_curriculum_1_1, 'prerequisites': [], 'summary': 'Introduction to programming using Python'},
    {'code': 'IS102-A', 'title': 'Computer Programming 2', 'units': 3, 'curriculum': bsis_curriculum_1_2, 'prerequisites': ['IS101-B'], 'summary': 'Object-oriented programming'},
    {'code': 'IS102-B', 'title': 'Data Structures and Algorithms', 'units': 3, 'curriculum': bsis_curriculum_1_2, 'prerequisites': ['IS101-B'], 'summary': 'Basic data structures'},
    {'code': 'IS201-A', 'title': 'Database Management Systems', 'units': 3, 'curriculum': bsis_curriculum_2_1, 'prerequisites': ['IS102-A'], 'summary': 'Relational databases and SQL'},
    {'code': 'IS201-B', 'title': 'Web Development 1', 'units': 3, 'curriculum': bsis_curriculum_2_1, 'prerequisites': ['IS102-A'], 'summary': 'Front-end web development basics'},
    {'code': 'IS202-A', 'title': 'Object-Oriented Programming', 'units': 3, 'curriculum': bsis_curriculum_2_2, 'prerequisites': ['IS102-A'], 'summary': 'Java or C++ OOP concepts'},
    {'code': 'IS202-B', 'title': 'Software Engineering 1', 'units': 3, 'curriculum': bsis_curriculum_2_2, 'prerequisites': ['IS201-A'], 'summary': 'Software development life cycle'},
    {'code': 'IS202-C', 'title': 'Web Development 2', 'units': 3, 'curriculum': bsis_curriculum_2_2, 'prerequisites': ['IS201-B'], 'summary': 'Server-side web development'},
    {'code': 'IS301-A', 'title': 'Operating Systems', 'units': 3, 'curriculum': bsis_curriculum_3_1, 'prerequisites': ['IS202-A'], 'summary': 'Concepts of OS and process management'},
    {'code': 'MATH301', 'title': 'Advanced Calculus', 'units': 3, 'curriculum': bsis_curriculum_3_1, 'prerequisites': ['MATH202'], 'summary': 'Differential Equations'},
    {'code': 'IS301-B', 'title': 'Computer Networks 1', 'units': 3, 'curriculum': bsis_curriculum_3_1, 'prerequisites': ['IS202-A'], 'summary': 'Networking concepts, TCP/IP model'},
    {'code': 'IS301-C', 'title': 'Human-Computer Interaction', 'units': 3, 'curriculum': bsis_curriculum_3_1, 'prerequisites': ['IS201-B'], 'summary': 'UI/UX design principles'},
    {'code': 'IS302-A', 'title': 'Computer Networks 2', 'units': 3, 'curriculum': bsis_curriculum_3_2, 'prerequisites': ['IS301-B'], 'summary': 'Advanced networking and security'},
    {'code': 'IS302-B', 'title': 'Mobile Application Development', 'units': 3, 'curriculum': bsis_curriculum_3_2, 'prerequisites': ['IS202-C'], 'summary': 'Developing apps for Android/iOS'},
    {'code': 'IS302-C', 'title': 'Information Assurance and Security', 'units': 3, 'curriculum': bsis_curriculum_3_2, 'prerequisites': ['IS301-B'], 'summary': 'Cybersecurity principles'},
    {'code': 'IS401-A', 'title': 'Capstone Project 1', 'units': 3, 'curriculum': bsis_curriculum_4_1, 'prerequisites': ['IS301-A', 'IS301-B', 'IS202-B'], 'summary': 'System design and initial development'},
    {'code': 'IS401-B', 'title': 'Systems Integration and Architecture', 'units': 3, 'curriculum': bsis_curriculum_4_1, 'prerequisites': ['IS302-A', 'IS201-A'], 'summary': 'Systems design and integration'},
    {'code': 'IS402-A', 'title': 'Capstone Project 2', 'units': 3, 'curriculum': bsis_curriculum_4_2, 'prerequisites': ['IS401-A'], 'summary': 'System implementation and defense'},
    {'code': 'IS402-B', 'title': 'Professional Ethics in IS', 'units': 3, 'curriculum': bsis_curriculum_4_2, 'prerequisites': [], 'summary': 'Ethical and legal issues in information systems'},
    {'code': 'IS402-C', 'title': 'Emerging Technologies', 'units': 3, 'curriculum': bsis_curriculum_4_2, 'prerequisites': [], 'summary': 'Trends in modern information systems'},

    # Information and Communications Technology (ICT) - 2-year program
    {'code': 'ICT101', 'title': 'Introduction to ICT', 'units': 3, 'curriculum': ict_curriculum_1_1, 'prerequisites': [], 'summary': 'Overview of information and communication technologies'},
    {'code': 'ICT102', 'title': 'Computer Hardware Servicing', 'units': 3, 'curriculum': ict_curriculum_1_2, 'prerequisites': ['ICT101'], 'summary': 'Hardware assembly and troubleshooting'},
    {'code': 'ICT201', 'title': 'Networking Fundamentals', 'units': 3, 'curriculum': ict_curriculum_2_1, 'prerequisites': ['ICT102'], 'summary': 'LAN/WAN concepts and network configuration'},
    {'code': 'ICT202', 'title': 'Web Development Fundamentals', 'units': 3, 'curriculum': ict_curriculum_2_2, 'prerequisites': ['ICT101'], 'summary': 'Basic front-end web design'},

    # Accountancy - BSAIS
    {'code': 'ACC101', 'title': 'Fundamentals of Accounting 1', 'units': 3, 'curriculum': bsais_curriculum_1_1, 'prerequisites': [], 'summary': 'Introduction to accounting concepts and principles'},
    {'code': 'ACC102', 'title': 'Fundamentals of Accounting 2', 'units': 3, 'curriculum': bsais_curriculum_1_2, 'prerequisites': ['ACC101'], 'summary': 'Continuation of basic accounting concepts'},
    {'code': 'ECON102', 'title': 'Introductory Macroeconomics', 'units': 3, 'curriculum': bsais_curriculum_1_2, 'prerequisites': [], 'summary': 'Explore Macroeconomics'},
    {'code': 'ACC201', 'title': 'Financial Accounting and Reporting 1', 'units': 3, 'curriculum': bsais_curriculum_2_1, 'prerequisites': ['ACC102'], 'summary': 'Preparation and presentation of financial statements'},
    {'code': 'ECON201', 'title': 'Microeconomics Theory and Applications', 'units': 3, 'curriculum': bsais_curriculum_2_1, 'prerequisites': ['ACC102'], 'summary': 'Preparation and presentation of financial statements'},
    {'code': 'ACC202', 'title': 'Financial Accounting and Reporting 2', 'units': 3, 'curriculum': bsais_curriculum_2_2, 'prerequisites': ['ACC201'], 'summary': 'Advanced financial accounting topics'},
    {'code': 'ACC301', 'title': 'Cost Accounting and Control', 'units': 3, 'curriculum': bsais_curriculum_3_1, 'prerequisites': ['ACC202'], 'summary': 'Cost accumulation and control systems'},
    {'code': 'ACC302', 'title': 'Management Accounting', 'units': 3, 'curriculum': bsais_curriculum_3_2, 'prerequisites': ['ACC301'], 'summary': 'Decision-making using accounting data'},
    {'code': 'AUD401', 'title': 'Auditing Theory and Practice', 'units': 3, 'curriculum': bsais_curriculum_4_1, 'prerequisites': ['ACC302'], 'summary': 'Auditing concepts and standards'},
    {'code': 'LAW401', 'title': 'Business Law and Taxation', 'units': 3, 'curriculum': bsais_curriculum_4_1, 'prerequisites': ['ACC302'], 'summary': 'Laws governing business and taxation'},

    # Tourism and Hospitality Management - BSTM
    {'code': 'TM101', 'title': 'Introduction to Tourism Industry', 'units': 3, 'curriculum': bstm_curriculum_1_1, 'prerequisites': [], 'summary': 'Overview of the tourism and hospitality industry'},
    {'code': 'TM102', 'title': 'Tourism Planning and Development', 'units': 3, 'curriculum': bstm_curriculum_1_2, 'prerequisites': ['TM101'], 'summary': 'Principles of tourism planning'},
    {'code': 'TM201', 'title': 'Travel Management Operations', 'units': 3, 'curriculum': bstm_curriculum_2_1, 'prerequisites': ['TM102'], 'summary': 'Tour operations and management practices'},
    {'code': 'HRM101', 'title': 'Introduction to Hospitality Management', 'units': 3, 'curriculum': bstm_curriculum_2_1, 'prerequisites': ['TM101'], 'summary': 'Foundations of hospitality operations'},
    {'code': 'TM202', 'title': 'Airline and Ticketing Procedures', 'units': 3, 'curriculum': bstm_curriculum_2_2, 'prerequisites': ['TM201'], 'summary': 'Airline systems and ticketing management'},
    {'code': 'MKT101', 'title': 'Principles of Marketing', 'units': 3, 'curriculum': bstm_curriculum_2_2, 'prerequisites': [], 'summary': 'Fundamentals of marketing concepts'},
    {'code': 'TM301', 'title': 'Tourism Policy and Planning', 'units': 3, 'curriculum': bstm_curriculum_3_1, 'prerequisites': ['TM102', 'TM201'], 'summary': 'Government policies and tourism planning frameworks'},
    {'code': 'HRM301', 'title': 'Food and Beverage Management', 'units': 3, 'curriculum': bstm_curriculum_3_1, 'prerequisites': ['HRM101'], 'summary': 'Operational management in food and beverage services'},
    {'code': 'TM302', 'title': 'Sustainable Tourism Development', 'units': 3, 'curriculum': bstm_curriculum_3_2, 'prerequisites': ['TM301'], 'summary': 'Sustainable practices in tourism and hospitality'},
    {'code': 'HRM302', 'title': 'Event Management', 'units': 3, 'curriculum': bstm_curriculum_3_2, 'prerequisites': ['HRM301'], 'summary': 'Planning and organizing hospitality and tourism events'},
    {'code': 'FIN401', 'title': 'Financial Management', 'units': 3, 'curriculum': bstm_curriculum_4_1, 'prerequisites': [], 'summary': 'Financial principles and decision-making'},
    {'code': 'TM401', 'title': 'Tourism and Hospitality Marketing', 'units': 3, 'curriculum': bstm_curriculum_4_2, 'prerequisites': ['MKT101', 'TM302'], 'summary': 'Marketing strategies for tourism and hospitality'},
    {'code': 'TM402', 'title': 'Tourism and Hospitality Management', 'units': 3, 'curriculum': bstm_curriculum_4_2, 'prerequisites': ['HRM302', 'TM301'], 'summary': 'Advanced management practices for tourism and hospitality operations'},

    # Civil Engineering - BSCE
    # FIRST YEAR - 1st Semester
    {'code': 'MATH101', 'title': 'Mathematics in the Modern World', 'units': 3, 'curriculum': bsce_curriculum_1_1, 'prerequisites': [], 'summary': 'Math in everyday life and decision-making'},
    {'code': 'ENG101', 'title': 'English Communication', 'units': 3, 'curriculum': bsce_curriculum_1_1, 'prerequisites': [], 'summary': 'English language skills and communication'},
    {'code': 'SELF101', 'title': 'Understanding the Self', 'units': 3, 'curriculum': bsce_curriculum_1_1, 'prerequisites': [], 'summary': 'Self-awareness and personal development'},
    {'code': 'CE101', 'title': 'Engineering Drawing and CAD', 'units': 3, 'curriculum': bsce_curriculum_1_1, 'prerequisites': [], 'summary': 'Technical drawing, orthographic projections, and computer-aided design fundamentals'},
    {'code': 'PE101', 'title': 'Physical Education 1', 'units': 2, 'curriculum': bsce_curriculum_1_1, 'prerequisites': [], 'summary': 'Basic physical fitness and wellness'},
    {'code': 'NSTP101', 'title': 'National Service Training Program 1', 'units': 3, 'curriculum': bsce_curriculum_1_1, 'prerequisites': [], 'summary': 'Civic welfare and community service training'},

    # FIRST YEAR - 2nd Semester
    {'code': 'MATH102', 'title': 'Calculus 1', 'units': 3, 'curriculum': bsce_curriculum_1_2, 'prerequisites': ['MATH101'], 'summary': 'Differential calculus, limits, derivatives, and applications'},
    {'code': 'CHEM101', 'title': 'Chemistry for Engineers', 'units': 3, 'curriculum': bsce_curriculum_1_2, 'prerequisites': [], 'summary': 'General chemistry principles and materials chemistry'},
    {'code': 'FIL101', 'title': 'Filipino 1', 'units': 3, 'curriculum': bsce_curriculum_1_2, 'prerequisites': [], 'summary': 'Pagbasa at pagsulat sa Filipino'},
    {'code': 'PCOM111', 'title': 'Purposive Communication', 'units': 3, 'curriculum': bsce_curriculum_1_2, 'prerequisites': ['ENG101'], 'summary': 'Professional and academic communication'},
    {'code': 'CE102', 'title': 'Engineering Mechanics - Statics', 'units': 3, 'curriculum': bsce_curriculum_1_2, 'prerequisites': ['MATH101'], 'summary': 'Forces, moments, equilibrium, free body diagrams, and structural analysis fundamentals'},
    {'code': 'PE102', 'title': 'Physical Education 2', 'units': 2, 'curriculum': bsce_curriculum_1_2, 'prerequisites': ['PE101'], 'summary': 'Team sports and activities'},
    {'code': 'NSTP102', 'title': 'National Service Training Program 2', 'units': 3, 'curriculum': bsce_curriculum_1_2, 'prerequisites': ['NSTP101'], 'summary': 'Advanced civic welfare and leadership training'},

    # SECOND YEAR - 1st Semester
    {'code': 'MATH201', 'title': 'Calculus 2', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': ['MATH102'], 'summary': 'Integral calculus and applications'},
    {'code': 'PHYS101', 'title': 'Physics for Engineers 1', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': ['MATH102'], 'summary': 'Mechanics, thermodynamics, and waves'},
    {'code': 'HIST101', 'title': 'Philippine History', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': [], 'summary': 'History of the Philippines'},
    {'code': 'CW201', 'title': 'The Contemporary World', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': [], 'summary': 'Globalization and international relations'},
    {'code': 'STAT101', 'title': 'Statistics and Probability', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': ['MATH101'], 'summary': 'Descriptive and inferential statistics'},
    {'code': 'CE201', 'title': 'Surveying 1', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': ['MATH102', 'CE101'], 'summary': 'Distance and angle measurement, leveling, traverse computations, and field work'},
    {'code': 'EM201', 'title': 'Engineering Mechanics - Dynamics', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': ['CE102', 'MATH102'], 'summary': 'Kinematics, kinetics, work-energy, and impulse-momentum principles'},
    {'code': 'MDB201', 'title': 'Mechanics of Deformable Bodies', 'units': 3, 'curriculum': bsce_curriculum_2_1, 'prerequisites': ['CE102'], 'summary': 'Stress, strain, axial loads, torsion, shear, and beam deflection'},
    {'code': 'PE201', 'title': 'Physical Education 3', 'units': 2, 'curriculum': bsce_curriculum_2_1, 'prerequisites': ['PE102'], 'summary': 'Individual and dual sports'},

    # SECOND YEAR - 2nd Semester
    {'code': 'MATH202', 'title': 'Differential Equations', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': ['MATH201'], 'summary': 'Ordinary and partial differential equations'},
    {'code': 'PHYS102', 'title': 'Physics for Engineers 2', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': ['PHYS101'], 'summary': 'Electricity, magnetism, and modern physics'},
    {'code': 'SCI101', 'title': 'Earth and Environmental Science', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': [], 'summary': 'Environmental awareness and sustainability'},
    {'code': 'STS211', 'title': 'Science, Technology and Society', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': [], 'summary': 'Impact of science and tech on society'},
    {'code': 'CE202', 'title': 'Surveying 2', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': ['CE201'], 'summary': 'Route surveying, topographic mapping, earthwork computations, and advanced surveying'},
    {'code': 'FMH202', 'title': 'Fluid Mechanics and Hydraulics', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': ['PHYS101', 'MATH201'], 'summary': 'Fluid properties, hydrostatics, fluid dynamics, and open channel flow'},
    {'code': 'ST202', 'title': 'Structural Theory 1', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': ['MDB201'], 'summary': 'Analysis of determinate structures, trusses, beams, and frames'},
    {'code': 'CMT202', 'title': 'Construction Materials and Testing', 'units': 3, 'curriculum': bsce_curriculum_2_2, 'prerequisites': ['CHEM101'], 'summary': 'Properties and testing of concrete, steel, aggregates, and construction materials'},
    {'code': 'PE202', 'title': 'Physical Education 4', 'units': 2, 'curriculum': bsce_curriculum_2_2, 'prerequisites': ['PE201'], 'summary': 'Recreational activities and fitness'},

    # THIRD YEAR - 1st Semester
    {'code': 'ETH301', 'title': 'Ethics', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': [], 'summary': 'Moral reasoning and ethical frameworks'},
    {'code': 'RES101', 'title': 'Research Methods 1', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': [], 'summary': 'Research writing and methodologies'},
    {'code': 'ELEC101', 'title': 'Elective 1', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': [], 'summary': 'Specialization elective subject'},
    {'code': 'CE301', 'title': 'Structural Theory 2', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': ['ST202'], 'summary': 'Analysis of indeterminate structures using moment distribution and slope-deflection methods'},
    {'code': 'GE301', 'title': 'Geotechnical Engineering 1', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': ['MDB201'], 'summary': 'Soil mechanics, classification, index properties, compaction, and permeability'},
    {'code': 'TE301', 'title': 'Transportation Engineering 1', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': ['CE202'], 'summary': 'Highway planning, geometric design, traffic engineering, and pavement design'},
    {'code': 'SD301', 'title': 'Principles of Steel Design', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': ['ST202'], 'summary': 'Design of steel tension members, beams, columns, and connections'},
    {'code': 'HYD301', 'title': 'Hydrology', 'units': 3, 'curriculum': bsce_curriculum_3_1, 'prerequisites': ['FMH202'], 'summary': 'Hydrologic cycle, precipitation, runoff, and flood frequency analysis'},

    # THIRD YEAR - 2nd Semester
    {'code': 'ART311', 'title': 'Art Appreciation', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': [], 'summary': 'Understanding and analyzing art forms'},
    {'code': 'RES102', 'title': 'Research Methods 2', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': ['RES101'], 'summary': 'Thesis proposal and defense'},
    {'code': 'ELEC102', 'title': 'Elective 2', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': [], 'summary': 'Specialization elective subject'},
    {'code': 'CE302', 'title': 'Reinforced Concrete Design 1', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': ['CE301', 'CMT202'], 'summary': 'Design of reinforced concrete beams, one-way slabs, and footings'},
    {'code': 'GE302', 'title': 'Geotechnical Engineering 2', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': ['GE301'], 'summary': 'Soil bearing capacity, settlement analysis, slope stability, and foundation engineering'},
    {'code': 'TE302', 'title': 'Transportation Engineering 2', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': ['TE301'], 'summary': 'Highway materials, pavement design, and construction methods'},
    {'code': 'WRE302', 'title': 'Water Resources Engineering', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': ['HYD301', 'FMH202'], 'summary': 'Water supply systems, irrigation, dams, and water resources planning'},
    {'code': 'ENV302', 'title': 'Environmental Engineering', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': ['SCI101', 'CHEM101'], 'summary': 'Water and wastewater treatment, solid waste management, and environmental impact'},
    {'code': 'CM302', 'title': 'Construction Methods and Project Management', 'units': 3, 'curriculum': bsce_curriculum_3_2, 'prerequisites': ['CMT202'], 'summary': 'Construction techniques, equipment, scheduling, and project management'},

    # FOURTH YEAR - 1st Semester
    {'code': 'MGT101', 'title': 'Principles of Management', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': [], 'summary': 'Basics of business and management'},
    {'code': 'ELEC201', 'title': 'Elective 3', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': [], 'summary': 'Specialization elective subject'},
    {'code': 'CE401', 'title': 'Reinforced Concrete Design 2', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': ['CE302'], 'summary': 'Design of columns, two-way slabs, stairs, and retaining walls'},
    {'code': 'SSD401', 'title': 'Structural Steel Design', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': ['SD301'], 'summary': 'Design of steel structures, frames, and industrial buildings'},
    {'code': 'FE401', 'title': 'Foundation Engineering', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': ['GE302'], 'summary': 'Design of shallow and deep foundations, pile foundations, and earth retaining structures'},
    {'code': 'BUS401', 'title': 'Building Utilities and Systems', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': [], 'summary': 'Plumbing, electrical, HVAC, fire protection, and building systems'},
    {'code': 'ECON401', 'title': 'Engineering Economics', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': [], 'summary': 'Time value of money, cost analysis, project evaluation, and feasibility studies'},
    {'code': 'LAW401CE', 'title': 'Civil Engineering Laws and Professional Practice', 'units': 3, 'curriculum': bsce_curriculum_4_1, 'prerequisites': [], 'summary': 'Philippine civil engineering laws, contracts, ethics, and professional practice'},

    # FOURTH YEAR - 2nd Semester
    {'code': 'PRAC101', 'title': 'On-the-Job Training (Internship)', 'units': 6, 'curriculum': bsce_curriculum_4_2, 'prerequisites': [], 'summary': 'Industry immersion and practicum'},
    {'code': 'CE402', 'title': 'Quantity Surveying and Cost Estimation', 'units': 3, 'curriculum': bsce_curriculum_4_2, 'prerequisites': ['CM302'], 'summary': 'Quantity take-off, cost estimation, bidding, and construction economics'},
    {'code': 'PCD402', 'title': 'Prestressed Concrete Design', 'units': 3, 'curriculum': bsce_curriculum_4_2, 'prerequisites': ['CE401'], 'summary': 'Pre-tensioned and post-tensioned concrete members and systems'},
    {'code': 'CAP402', 'title': 'Civil Engineering Design Project (Capstone)', 'units': 3, 'curriculum': bsce_curriculum_4_2, 'prerequisites': ['CE401', 'SSD401', 'FE401'], 'summary': 'Comprehensive design project integrating all civil engineering disciplines'},
    {'code': 'SEM402', 'title': 'Seminars and Current Issues in Civil Engineering', 'units': 2, 'curriculum': bsce_curriculum_4_2, 'prerequisites': [], 'summary': 'Contemporary challenges, innovations, and emerging trends in civil engineering'},

    # Criminology - BSCRIM
    {'code': 'CRIM101', 'title': 'Introduction to Criminology', 'units': 3, 'curriculum': bscrim_curriculum_1_1, 'prerequisites': [], 'summary': 'Nature and scope of criminology'},
    {'code': 'CRIM102', 'title': 'Philippine Criminal Justice System', 'units': 3, 'curriculum': bscrim_curriculum_1_2, 'prerequisites': ['CRIM101'], 'summary': 'Structure and function of the justice system'},
    {'code': 'CRIM201', 'title': 'Law Enforcement Administration', 'units': 3, 'curriculum': bscrim_curriculum_2_1, 'prerequisites': ['CRIM102'], 'summary': 'Principles of police organization and management'},
    {'code': 'LAW201', 'title': 'Criminal Law Book 1', 'units': 3, 'curriculum': bscrim_curriculum_2_2, 'prerequisites': ['CRIM102'], 'summary': 'Study of the Revised Penal Code Book 1'},
    {'code': 'CRIM301', 'title': 'Criminal Investigation', 'units': 3, 'curriculum': bscrim_curriculum_3_1, 'prerequisites': ['CRIM201', 'LAW201'], 'summary': 'Techniques and procedures in criminal investigation'},
    {'code': 'LAW301', 'title': 'Criminal Law Book 2', 'units': 3, 'curriculum': bscrim_curriculum_3_1, 'prerequisites': ['LAW201'], 'summary': 'Study of the Revised Penal Code Book 2'},
    {'code': 'CRIM302', 'title': 'Forensic Science', 'units': 3, 'curriculum': bscrim_curriculum_3_2, 'prerequisites': ['CRIM301'], 'summary': 'Scientific methods in crime scene investigation'},
    {'code': 'PSY302', 'title': 'Forensic Psychology', 'units': 3, 'curriculum': bscrim_curriculum_3_2, 'prerequisites': [], 'summary': 'Psychology applied to criminal behavior'},
    {'code': 'CRIM401', 'title': 'Criminalistics', 'units': 3, 'curriculum': bscrim_curriculum_4_1, 'prerequisites': ['CRIM302'], 'summary': 'Scientific crime detection techniques'},
    {'code': 'PSY402', 'title': 'Criminological Theories', 'units': 3, 'curriculum': bscrim_curriculum_4_2, 'prerequisites': ['CRIM101'], 'summary': 'Theories of crime causation'},

    # Nursing - BSN
    {'code': 'NURS101', 'title': 'Theoretical Foundations of Nursing', 'units': 3, 'curriculum': bsn_curriculum_1_1, 'prerequisites': [], 'summary': 'Nursing history, theories, and principles'},
    {'code': 'BIO101', 'title': 'Anatomy and Physiology 1', 'units': 3, 'curriculum': bsn_curriculum_1_1, 'prerequisites': [], 'summary': 'Human anatomy and basic physiology'},
    {'code': 'NURS102', 'title': 'Health Assessment', 'units': 3, 'curriculum': bsn_curriculum_1_2, 'prerequisites': ['BIO101'], 'summary': 'Techniques in physical and health assessment'},
    {'code': 'BIO102', 'title': 'Anatomy and Physiology 2', 'units': 3, 'curriculum': bsn_curriculum_1_2, 'prerequisites': ['BIO101'], 'summary': 'Continuation of human anatomy and physiology'},
    {'code': 'NCM201', 'title': 'Fundamentals of Nursing Practice', 'units': 3, 'curriculum': bsn_curriculum_2_1, 'prerequisites': ['NURS101', 'NURS102'], 'summary': 'Nursing process, basic skills, and foundational care'},
    {'code': 'NCM202', 'title': 'Pharmacology', 'units': 3, 'curriculum': bsn_curriculum_2_2, 'prerequisites': ['BIO102'], 'summary': 'Drug classifications, safe medication administration, and dosage calculations'},
    {'code': 'NCM301', 'title': 'Nursing Care Management 1', 'units': 3, 'curriculum': bsn_curriculum_3_1, 'prerequisites': ['NCM201', 'NCM202'], 'summary': 'Care of clients with altered oxygenation, nutrition, and elimination'},
    {'code': 'NCM302', 'title': 'Nursing Care Management 2', 'units': 3, 'curriculum': bsn_curriculum_3_2, 'prerequisites': ['NCM301'], 'summary': 'Maternal and child health nursing and community exposure'},
    {'code': 'NCM401', 'title': 'Nursing Care Management 3', 'units': 3, 'curriculum': bsn_curriculum_4_1, 'prerequisites': ['NCM302'], 'summary': 'Care of clients with psychosocial and behavioral problems (Psychiatric Nursing)'},
    {'code': 'NCM402', 'title': 'Nursing Leadership and Management', 'units': 3, 'curriculum': bsn_curriculum_4_2, 'prerequisites': ['NCM401'], 'summary': 'Nursing administration, leadership, and research practicum'},

    # Entrepreneurship - BSEntrep
    {'code': 'ENT101', 'title': 'Introduction to Entrepreneurship', 'units': 3, 'curriculum': bsentrep_curriculum_1_1, 'prerequisites': [], 'summary': 'Fundamentals of entrepreneurship and business creation'},
    {'code': 'ENT102', 'title': 'Business Planning and Feasibility', 'units': 3, 'curriculum': bsentrep_curriculum_1_2, 'prerequisites': ['ENT101'], 'summary': 'Business plan development and feasibility studies'},
    {'code': 'ENT201', 'title': 'Marketing Management', 'units': 3, 'curriculum': bsentrep_curriculum_2_1, 'prerequisites': ['ENT102'], 'summary': 'Marketing strategies for new ventures'},
    {'code': 'ENT202', 'title': 'Financial Management for Entrepreneurs', 'units': 3, 'curriculum': bsentrep_curriculum_2_2, 'prerequisites': ['ENT201'], 'summary': 'Financial planning and management for startups'},
    {'code': 'ENT301', 'title': 'Operations Management', 'units': 3, 'curriculum': bsentrep_curriculum_3_1, 'prerequisites': ['ENT202'], 'summary': 'Business operations and process management'},
    {'code': 'ENT302', 'title': 'Innovation and Product Development', 'units': 3, 'curriculum': bsentrep_curriculum_3_2, 'prerequisites': ['ENT301'], 'summary': 'Innovation strategies and new product development'},
    {'code': 'ENT401', 'title': 'Business Venture Creation', 'units': 3, 'curriculum': bsentrep_curriculum_4_1, 'prerequisites': ['ENT302'], 'summary': 'Launching and managing new business ventures'},
    {'code': 'ENT402', 'title': 'Social Entrepreneurship', 'units': 3, 'curriculum': bsentrep_curriculum_4_2, 'prerequisites': ['ENT401'], 'summary': 'Creating businesses with social impact'},

    # Culture and Arts Education - BCED
    {'code': 'ART101', 'title': 'Introduction to Arts Education', 'units': 3, 'curriculum': bced_curriculum_1_1, 'prerequisites': [], 'summary': 'Foundations of arts education and pedagogy'},
    {'code': 'ART102', 'title': 'Visual Arts Fundamentals', 'units': 3, 'curriculum': bced_curriculum_1_2, 'prerequisites': ['ART101'], 'summary': 'Basic visual arts techniques and principles'},
    {'code': 'ART201', 'title': 'Music Education', 'units': 3, 'curriculum': bced_curriculum_2_1, 'prerequisites': ['ART102'], 'summary': 'Music theory and teaching methods'},
    {'code': 'ART202', 'title': 'Dance and Movement Education', 'units': 3, 'curriculum': bced_curriculum_2_2, 'prerequisites': ['ART201'], 'summary': 'Dance pedagogy and choreography basics'},
    {'code': 'ART301', 'title': 'Theater Arts Education', 'units': 3, 'curriculum': bced_curriculum_3_1, 'prerequisites': ['ART202'], 'summary': 'Drama and theater teaching methods'},
    {'code': 'ART302', 'title': 'Filipino Arts and Culture', 'units': 3, 'curriculum': bced_curriculum_3_2, 'prerequisites': ['ART301'], 'summary': 'Philippine indigenous and contemporary arts'},
    {'code': 'ART401', 'title': 'Arts Curriculum Development', 'units': 3, 'curriculum': bced_curriculum_4_1, 'prerequisites': ['ART302'], 'summary': 'Designing arts education programs'},
    {'code': 'ART402', 'title': 'Arts Practicum and Teaching', 'units': 3, 'curriculum': bced_curriculum_4_2, 'prerequisites': ['ART401'], 'summary': 'Supervised teaching practice in arts education'},

    # Technical-Vocational Teacher Education - BTVTED
    {'code': 'TVT101', 'title': 'Introduction to Technical Education', 'units': 3, 'curriculum': btvted_curriculum_1_1, 'prerequisites': [], 'summary': 'Foundations of technical-vocational education'},
    {'code': 'TVT102', 'title': 'Workshop Safety and Management', 'units': 3, 'curriculum': btvted_curriculum_1_2, 'prerequisites': ['TVT101'], 'summary': 'Safety protocols and workshop organization'},
    {'code': 'TVT201', 'title': 'Technical Drawing and Design', 'units': 3, 'curriculum': btvted_curriculum_2_1, 'prerequisites': ['TVT102'], 'summary': 'Technical drafting and design principles'},
    {'code': 'TVT202', 'title': 'Industrial Materials and Processes', 'units': 3, 'curriculum': btvted_curriculum_2_2, 'prerequisites': ['TVT201'], 'summary': 'Materials science and manufacturing processes'},
    {'code': 'TVT301', 'title': 'Vocational Teaching Methods', 'units': 3, 'curriculum': btvted_curriculum_3_1, 'prerequisites': ['TVT202'], 'summary': 'Pedagogical approaches for technical education'},
    {'code': 'TVT302', 'title': 'Competency-Based Assessment', 'units': 3, 'curriculum': btvted_curriculum_3_2, 'prerequisites': ['TVT301'], 'summary': 'Skills assessment and evaluation methods'},
    {'code': 'TVT401', 'title': 'Industry Practicum', 'units': 3, 'curriculum': btvted_curriculum_4_1, 'prerequisites': ['TVT302'], 'summary': 'Industry immersion and skills development'},
    {'code': 'TVT402', 'title': 'TVET Curriculum Development', 'units': 3, 'curriculum': btvted_curriculum_4_2, 'prerequisites': ['TVT401'], 'summary': 'Developing technical-vocational curricula'},

    # Tourism & Hospitality Management Technology (TTHMT) - 3-year
    {'code': 'TH101', 'title': 'Introduction to Tourism and Hospitality Technology', 'units': 3, 'curriculum': tthmt_curriculum_1_1, 'prerequisites': [], 'summary': 'Overview of tourism and hospitality technology applications'},
    {'code': 'TH102', 'title': 'Fundamentals of Hospitality Operations', 'units': 3, 'curriculum': tthmt_curriculum_1_2, 'prerequisites': ['TH101'], 'summary': 'Basic hospitality management and operations principles'},
    {'code': 'TH201', 'title': 'Travel and Tour Operations Technology', 'units': 3, 'curriculum': tthmt_curriculum_2_1, 'prerequisites': ['TH102'], 'summary': 'Tour operations systems and technology integration'},
    {'code': 'TH202', 'title': 'Airline and Ticketing Systems', 'units': 3, 'curriculum': tthmt_curriculum_2_2, 'prerequisites': ['TH201'], 'summary': 'Technological systems used in airline and booking management'},
    {'code': 'TH301', 'title': 'Hospitality Systems Management', 'units': 3, 'curriculum': tthmt_curriculum_3_1, 'prerequisites': ['TH202'], 'summary': 'Systems management in tourism and hospitality enterprises'},
    {'code': 'TH302', 'title': 'Sustainable Tourism Practices', 'units': 3, 'curriculum': tthmt_curriculum_3_2, 'prerequisites': ['TH301'], 'summary': 'Sustainability and innovation in tourism and hospitality technology'},

    # Business & Financial Data Information Systems (BFDIS) - 3-year
    {'code': 'BF101', 'title': 'Introduction to Business Information Systems', 'units': 3, 'curriculum': bfdis_curriculum_1_1, 'prerequisites': [], 'summary': 'Overview of business processes and information systems'},
    {'code': 'BF102', 'title': 'Business Computing Fundamentals', 'units': 3, 'curriculum': bfdis_curriculum_1_2, 'prerequisites': ['BF101'], 'summary': 'Introduction to computing tools and data management for business'},
    {'code': 'BF201', 'title': 'Financial Data Analysis', 'units': 3, 'curriculum': bfdis_curriculum_2_1, 'prerequisites': ['BF102'], 'summary': 'Analytical techniques for interpreting financial data'},
    {'code': 'BF202', 'title': 'Database Systems for Business', 'units': 3, 'curriculum': bfdis_curriculum_2_2, 'prerequisites': ['BF201'], 'summary': 'Design and management of databases in financial contexts'},
    {'code': 'BF301', 'title': 'Business Intelligence and Reporting', 'units': 3, 'curriculum': bfdis_curriculum_3_1, 'prerequisites': ['BF202'], 'summary': 'Decision-making using business intelligence tools'},
    {'code': 'BF302', 'title': 'Enterprise Systems and Financial Integration', 'units': 3, 'curriculum': bfdis_curriculum_3_2, 'prerequisites': ['BF301'], 'summary': 'Enterprise resource planning and financial data systems integration'},

    # Hospitality & Restaurant Services (HRS) - 2-year
    {'code': 'HRS101', 'title': 'Introduction to Hospitality and Restaurant Services', 'units': 3, 'curriculum': hrs_curriculum_1_1, 'prerequisites': [], 'summary': 'Overview of hospitality industry operations and service fundamentals'},
    {'code': 'HRS102', 'title': 'Food and Beverage Service Operations', 'units': 3, 'curriculum': hrs_curriculum_1_2, 'prerequisites': ['HRS101'], 'summary': 'Principles and techniques in food and beverage service'},
    {'code': 'HRS201', 'title': 'Front Office Management', 'units': 3, 'curriculum': hrs_curriculum_2_1, 'prerequisites': ['HRS102'], 'summary': 'Front desk operations and guest relations management'},
    {'code': 'HRS202', 'title': 'Culinary and Kitchen Operations', 'units': 3, 'curriculum': hrs_curriculum_2_2, 'prerequisites': ['HRS201'], 'summary': 'Food preparation, kitchen management, and safety practices'},

    # Culinary & Restaurant Services (CRS) - 2-year
    {'code': 'CRS101', 'title': 'Fundamentals of Culinary Arts', 'units': 3, 'curriculum': crs_curriculum_1_1, 'prerequisites': [], 'summary': 'Introduction to cooking principles and culinary techniques'},
    {'code': 'CRS102', 'title': 'Restaurant Service and Etiquette', 'units': 3, 'curriculum': crs_curriculum_1_2, 'prerequisites': ['CRS101'], 'summary': 'Service procedures, customer interaction, and dining etiquette'},
    {'code': 'CRS201', 'title': 'Advanced Culinary Techniques', 'units': 3, 'curriculum': crs_curriculum_2_1, 'prerequisites': ['CRS102'], 'summary': 'Menu planning, advanced cooking methods, and kitchen management'},
    {'code': 'CRS202', 'title': 'Catering and Restaurant Management', 'units': 3, 'curriculum': crs_curriculum_2_2, 'prerequisites': ['CRS201'], 'summary': 'Catering operations, event planning, and restaurant supervision'},

    # Business Office & Accounting Technology (BOAT) - 2-year
    {'code': 'BOA101', 'title': 'Fundamentals of Office Procedures', 'units': 3, 'curriculum': boat_curriculum_1_1, 'prerequisites': [], 'summary': 'Office organization, documentation, and clerical management'},
    {'code': 'BOA102', 'title': 'Basic Accounting Principles', 'units': 3, 'curriculum': boat_curriculum_1_2, 'prerequisites': ['BOA101'], 'summary': 'Introduction to financial accounting and bookkeeping'},
    {'code': 'BOA201', 'title': 'Business Communication and Document Processing', 'units': 3, 'curriculum': boat_curriculum_2_1, 'prerequisites': ['BOA102'], 'summary': 'Professional communication and document handling in business settings'},
    {'code': 'BOA202', 'title': 'Computerized Accounting Systems', 'units': 3, 'curriculum': boat_curriculum_2_2, 'prerequisites': ['BOA201'], 'summary': 'Accounting applications using modern software systems'},

    # Salon, Spa & Wellness Technology (SSWT) - 2-year
    {'code': 'SSW101', 'title': 'Introduction to Beauty and Wellness', 'units': 3, 'curriculum': sswt_curriculum_1_1, 'prerequisites': [], 'summary': 'Overview of salon, spa, and wellness services'},
    {'code': 'SSW102', 'title': 'Basic Hair and Skin Care', 'units': 3, 'curriculum': sswt_curriculum_1_2, 'prerequisites': ['SSW101'], 'summary': 'Fundamentals of hair, facial, and skin treatments'},
    {'code': 'SSW201', 'title': 'Massage and Body Therapy Techniques', 'units': 3, 'curriculum': sswt_curriculum_2_1, 'prerequisites': ['SSW102'], 'summary': 'Massage theory, body care procedures, and spa operations'},
    {'code': 'SSW202', 'title': 'Salon and Spa Management', 'units': 3, 'curriculum': sswt_curriculum_2_2, 'prerequisites': ['SSW201'], 'summary': 'Managing salon and spa businesses, client relations, and service quality'},

    # ========================================
    # BSIS - Bachelor of Science in Information Systems (BSIS)
    # ----------------------------------------
    # Enrollment: {'student': '2021-00002', 'section': 'BSIS-3-2', 'subject': 'IT303', 'term': '2nd'}
    {'code': 'IT303', 'title': 'Information Technology Elective 3', 'units': 3, 'prerequisites': ['IS201-B'], 'summary': 'IT elective focusing on advanced topics.', 'curriculum': bsis_curriculum_3_2},
    # Enrollment: {'student': '2021-00002', 'section': 'BSIS-3-2', 'subject': 'ENG301', 'term': '2nd'}
    {'code': 'ENG302', 'title': 'Technical Writing and Reporting', 'units': 3, 'prerequisites': ['ENG201'], 'summary': 'Principles of professional and technical communication.', 'curriculum': bsis_curriculum_3_2},
    # Enrollment: {'student': '2023-00010', 'section': 'BSIS-1-1', 'subject': 'IS102-A', 'term': '1st'}
    {'code': 'IS102-A', 'title': 'Introduction to Programming (Lab)', 'units': 1, 'prerequisites': ['IS101-A'], 'summary': 'Hands-on practice for basic programming concepts.', 'curriculum': bsis_curriculum_1_1},
    # Enrollment: {'student': '2023-00014', 'section': 'BSIS-1-1', 'subject': 'IS101-C', 'term': '1st'}
    {'code': 'IS101-C', 'title': 'Computer Fundamentals (Lecture)', 'units': 3, 'prerequisites': [], 'summary': 'Basic concepts of computing hardware, software, and systems.', 'curriculum': bsis_curriculum_1_1},

    # ========================================
    # BSAIS - Bachelor of Science in Accounting Information Systems (BSAIS)
    # ----------------------------------------
    # Enrollment: {'student': '2022-00007', 'section': 'BSAIS-2-2', 'subject': 'ACC203', 'term': '2nd'}
    {'code': 'ACC203', 'title': 'Intermediate Accounting Part 1', 'units': 3, 'prerequisites': ['ACC201'], 'summary': 'In-depth study of financial accounting standards.', 'curriculum': bsais_curriculum_2_2},
    # Enrollment: {'student': '2022-00011', 'section': 'BSAIS-2-2', 'subject': 'ACC204', 'term': '2nd'}
    {'code': 'ACC204', 'title': 'Intermediate Accounting Part 2', 'units': 3, 'prerequisites': ['ACC202'], 'summary': 'Continuation of intermediate accounting topics.', 'curriculum': bsais_curriculum_2_2},
    # Enrollment: {'student': '2021-00020', 'section': 'BSAIS-4-1', 'subject': 'ACC401', 'term': '1st'}
    {'code': 'ACC401', 'title': 'Advanced Accounting Part 1', 'units': 3, 'prerequisites': ['ACC301'], 'summary': 'Accounting for special transactions and entities.', 'curriculum': bsais_curriculum_4_1},

    # ========================================
    # ICT - Information and Communication Technology (ICT) (2-Year Program)
    # ----------------------------------------
    # Enrollment: {'student': '2023-00004', 'section': 'ICT-1-1', 'subject': 'COMP101', 'term': '1st'}
    {'code': 'COMP101', 'title': 'Computer Programming 1', 'units': 3, 'prerequisites': [], 'summary': 'Foundational course in programming logic and language.', 'curriculum': ict_curriculum_1_1},
    # Enrollment: {'student': '2021-00012', 'section': 'ICT-2-1', 'subject': 'ICT301', 'term': '1st'} (Assuming this is a 2nd year student taking a 300-level course)
    {'code': 'ICT301', 'title': 'Data Communications and Networking', 'units': 3, 'prerequisites': ['ICT201'], 'summary': 'Principles of data transmission and network protocols.', 'curriculum': ict_curriculum_2_1},
    # Enrollment: {'student': '2021-00012', 'section': 'ICT-2-1', 'subject': 'COMP301', 'term': '1st'}
    {'code': 'COMP301', 'title': 'Advanced Data Structures', 'units': 3, 'prerequisites': ['COMP101'], 'summary': 'Complex data structures and algorithms.', 'curriculum': ict_curriculum_2_1},
    # Enrollment: {'student': '2021-00012', 'section': 'ICT-2-1', 'subject': 'NET301', 'term': '1st'}
    {'code': 'NET301', 'title': 'Network Design and Implementation', 'units': 3, 'prerequisites': ['ICT301'], 'summary': 'Practical skills in designing and setting up networks.', 'curriculum': ict_curriculum_2_1},

    # ========================================
    # BSTM - Bachelor of Science in Tourism Management (BSTM)
    # ----------------------------------------
    # Enrollment: {'student': '2022-00005', 'section': 'BSTM-2-1', 'subject': 'MKT201', 'term': '1st'}
    {'code': 'MKT201', 'title': 'Principles of Marketing', 'units': 3, 'prerequisites': [], 'summary': 'Basic concepts and theories of marketing.', 'curriculum': bstm_curriculum_2_1},
    # Enrollment: {'student': '2022-00005', 'section': 'BSTM-2-1', 'subject': 'HRM201', 'term': '1st'}
    {'code': 'HRM201', 'title': 'Fundamentals of Human Resource Management', 'units': 3, 'prerequisites': ['HRM101'], 'summary': 'Introduction to HR functions and practices.', 'curriculum': bstm_curriculum_2_1},
    # Enrollment: {'student': '2021-00008', 'section': 'BSTM-4-1', 'subject': 'MKT401', 'term': '1st'}
    {'code': 'MKT401', 'title': 'Strategic Marketing in Tourism', 'units': 3, 'prerequisites': ['MKT201'], 'summary': 'Applying marketing strategy in the tourism sector.', 'curriculum': bstm_curriculum_4_1},
    # Enrollment: {'student': '2022-00015', 'section': 'BSTM-2-2', 'subject': 'HRM202', 'term': '2nd'}
    {'code': 'HRM202', 'title': 'Organizational Behavior in Tourism', 'units': 3, 'prerequisites': ['HRM201'], 'summary': 'Studying human behavior in tourism organizations.', 'curriculum': bstm_curriculum_2_2},
    # Enrollment: {'student': '2022-00015', 'section': 'BSTM-2-2', 'subject': 'MKT202', 'term': '2nd'}
    {'code': 'MKT202', 'title': 'Marketing for Hospitality and Tourism', 'units': 3, 'prerequisites': ['MKT201'], 'summary': 'Specialized marketing techniques for the industry.', 'curriculum': bstm_curriculum_2_2},
    # Enrollment: {'student': '2023-00019', 'section': 'BSTM-1-1', 'subject': 'HRM101', 'term': '1st'}
    {'code': 'HRM101', 'title': 'Introduction to Hospitality Management', 'units': 3, 'prerequisites': [], 'summary': 'Survey of the hospitality industry and management roles.', 'curriculum': bstm_curriculum_1_1},
    # Enrollment: {'student': '2023-00019', 'section': 'BSTM-1-1', 'subject': 'MKT101', 'term': '1st'}
    {'code': 'MKT101', 'title': 'Fundamentals of Tourism Marketing', 'units': 3, 'prerequisites': [], 'summary': 'Basic marketing principles in the context of tourism.', 'curriculum': bstm_curriculum_1_1},

    # ========================================
    # BSCRIM - Bachelor of Science in Criminology (BSCRIM)
    # ----------------------------------------
    # Enrollment: {'student': '2023-00006', 'section': 'BSCRIM-1-1', 'subject': 'LAW101', 'term': '1st'}
    {'code': 'LAW101', 'title': 'Criminal Law and Jurisprudence', 'units': 3, 'prerequisites': [], 'summary': 'Basic principles of criminal law and legal system.', 'curriculum': bscrim_curriculum_1_1},
    # Enrollment: {'student': '2022-00013', 'section': 'BSCRIM-2-1', 'subject': 'PSY201', 'term': '1st'}
    {'code': 'PSY201', 'title': 'Forensic Psychology', 'units': 3, 'prerequisites': [], 'summary': 'Application of psychological principles to the justice system.', 'curriculum': bscrim_curriculum_2_1},
    # Enrollment: {'student': '2021-00017', 'section': 'BSCRIM-4-1', 'subject': 'LAW401', 'term': '1st'}
    {'code': 'LAW401', 'title': 'Legal Forms and Procedure', 'units': 3, 'prerequisites': ['CRIM201'], 'summary': 'Preparation of legal documents and court procedures.', 'curriculum': bscrim_curriculum_4_1},
    # Enrollment: {'student': '2021-00017', 'section': 'BSCRIM-4-2', 'subject': 'PSY401', 'term': '2nd'}
    {'code': 'PSY401', 'title': 'Criminal Behavior and Profiling', 'units': 3, 'prerequisites': ['PSY201'], 'summary': 'Theories of criminal behavior and offender profiling.', 'curriculum': bscrim_curriculum_4_2},

    # ========================================
    # BSN - Bachelor of Science in Nursing (BSN)
    # ----------------------------------------
    # Enrollment: {'student': '2021-00009', 'section': 'BSN-4-1', 'subject': 'NURS401', 'term': '1st'}
    {'code': 'NURS401', 'title': 'Clinical Duty 4 (Advanced)', 'units': 6, 'prerequisites': ['NCM202'], 'summary': 'Advanced clinical practice and patient care.', 'curriculum': bsn_curriculum_4_1},
    # Enrollment: {'student': '2021-00009', 'section': 'BSN-4-1', 'subject': 'BIO401', 'term': '1st'}
    {'code': 'BIO401', 'title': 'Pathophysiology', 'units': 3, 'prerequisites': ['BIO101'], 'summary': 'The study of the functional changes associated with disease and injury.', 'curriculum': bsn_curriculum_4_1},
    # Enrollment: {'student': '2021-00009', 'section': 'BSN-4-1', 'subject': 'ANAT401', 'term': '1st'}
    {'code': 'ANAT401', 'title': 'Advanced Human Anatomy and Physiology', 'units': 3, 'prerequisites': ['ANAT101'], 'summary': 'In-depth study of the human body structure and function.', 'curriculum': bsn_curriculum_4_1},
    # Enrollment: {'student': '2023-00016', 'section': 'BSN-1-1', 'subject': 'ANAT101', 'term': '1st'}
    {'code': 'ANAT101', 'title': 'Basic Human Anatomy and Physiology', 'units': 3, 'prerequisites': ['BIO101'], 'summary': 'Foundational study of the structure and function of the human body.', 'curriculum': bsn_curriculum_1_1},

    

]


subjects = {}
for data in subjects_data:
    subject, created = Subject.objects.get_or_create(
        code=data['code'],
        defaults={
            'title': data['title'],
            'units': data['units'],
            'curriculum': data['curriculum'],
            'prerequisites': data.get('prerequisites', []),
            'summary': data.get('summary', '')
        }
    )
    subjects[data['code']] = subject
    status = "✅ Created" if created else "⏭️  Exists"
    print(f"  {status}: {data['code']} - {data['title']} ({data['units']} units)")

print(f"\n✅ Total Subjects: {len(subjects)}\n")

# ========================================
# 6. SAMPLE section (Fixed with valid professors)
# ========================================
print("🏫 Creating Sample section_names for Term 2024-2025-1st...")

sections_data = [
    # -------------------------------
    # 4-YEAR PROGRAMS
    # -------------------------------

    # BSIS (Information Systems) - year1..4 (1st sem)
    {'section_name': 'BSIS-1-1', 'subject': 'IS101-A', 'term': '2024-2025-1st', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 8:00-9:00 AM',  'room': 'CS-101'},
    {'section_name': 'BSIS-1-1', 'subject': 'IS101-B', 'term': '2024-2025-1st', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 9:00-10:00 AM', 'room': 'CS-102'},
    {'section_name': 'BSIS-2-1', 'subject': 'IS201-A', 'term': '2024-2025-1st', 'professor': 'prof_africa',   'schedule': 'TTH 10:00-11:30 AM','room': 'CS-201'},
    {'section_name': 'BSIS-2-1', 'subject': 'IS201-B', 'term': '2024-2025-1st', 'professor': 'prof_africa',   'schedule': 'TTH 11:30-1:00 PM', 'room': 'CS-202'},
    {'section_name': 'BSIS-3-1', 'subject': 'IS301-A', 'term': '2024-2025-1st', 'professor': 'prof_cenita',   'schedule': 'MWF 9:00-10:00 AM', 'room': 'CS-301'},
    {'section_name': 'BSIS-3-1', 'subject': 'IS301-B', 'term': '2024-2025-1st', 'professor': 'prof_cenita',   'schedule': 'MWF 10:00-11:00 AM','room': 'CS-302'},
    {'section_name': 'BSIS-3-1', 'subject': 'IS301-C', 'term': '2024-2025-1st', 'professor': 'prof_cenita',   'schedule': 'MWF 11:00-12:00 NN','room': 'CS-303'},
    {'section_name': 'BSIS-4-1', 'subject': 'IS401-A', 'term': '2024-2025-1st', 'professor': 'prof_delmonte', 'schedule': 'TTH 1:00-2:30 PM',  'room': 'CS-401'},
    {'section_name': 'BSIS-4-1', 'subject': 'IS401-B', 'term': '2024-2025-1st', 'professor': 'prof_delmonte', 'schedule': 'TTH 2:30-4:00 PM',  'room': 'CS-402'},
    
    
    # BSIS (Information Systems) - year1..4 (2nd sem)
    {'section_name': 'BSIS-1-2', 'subject': 'IS102-A', 'term': '2024-2025-2nd', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 10:00-11:00 AM', 'room': 'CS-103'},
    {'section_name': 'BSIS-1-2', 'subject': 'IS102-B', 'term': '2024-2025-2nd', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 11:00-12:00 NN', 'room': 'CS-104'},
    {'section_name': 'BSIS-2-2', 'subject': 'IS202-A', 'term': '2024-2025-2nd', 'professor': 'prof_africa',   'schedule': 'TTH 1:00-2:30 PM', 'room': 'CS-203'},
    {'section_name': 'BSIS-2-2', 'subject': 'IS202-B', 'term': '2024-2025-2nd', 'professor': 'prof_africa',   'schedule': 'TTH 2:30-4:00 PM', 'room': 'CS-204'},
    {'section_name': 'BSIS-2-2', 'subject': 'IS202-C', 'term': '2024-2025-2nd', 'professor': 'prof_africa',   'schedule': 'TTH 4:00-5:30 PM', 'room': 'CS-205'},
    {'section_name': 'BSIS-3-2', 'subject': 'IS302-A', 'term': '2024-2025-2nd', 'professor': 'prof_cenita',   'schedule': 'MWF 8:00-9:00 AM', 'room': 'CS-303'},
    {'section_name': 'BSIS-3-2', 'subject': 'IS302-B', 'term': '2024-2025-2nd', 'professor': 'prof_cenita',   'schedule': 'MWF 9:00-10:00 AM', 'room': 'CS-304'},
    {'section_name': 'BSIS-3-2', 'subject': 'IS302-C', 'term': '2024-2025-2nd', 'professor': 'prof_cenita',   'schedule': 'MWF 10:00-11:00 AM', 'room': 'CS-305'},
    {'section_name': 'BSIS-4-2', 'subject': 'IS402-A', 'term': '2024-2025-2nd', 'professor': 'prof_delmonte', 'schedule': 'TTH 9:30-11:00 AM', 'room': 'CS-403'},
    {'section_name': 'BSIS-4-2', 'subject': 'IS402-B', 'term': '2024-2025-2nd', 'professor': 'prof_delmonte', 'schedule': 'TTH 11:00-12:30 NN', 'room': 'CS-404'},
    {'section_name': 'BSIS-4-2', 'subject': 'IS402-C', 'term': '2024-2025-2nd', 'professor': 'prof_delmonte', 'schedule': 'TTH 1:00-2:30 PM', 'room': 'CS-405'},

    # BSN (Nursing) year1..4 (1st sem)
    {'section_name': 'BSN-1-1', 'subject': 'NURS101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'MWF 7:30-8:30 AM', 'room': 'NUR-101'},
    {'section_name': 'BSN-1-1', 'subject': 'BIO101', 'term': '2024-2025-1st', 'professor': 'prof_garcia', 'schedule': 'TTH 8:00-9:30 AM', 'room': 'NUR-102'},
    {'section_name': 'BSN-2-1', 'subject': 'NCM201', 'term': '2024-2025-1st', 'professor': 'prof_reyes',  'schedule': 'TTH 9:30-11:00 AM', 'room': 'NUR-201'},
    {'section_name': 'BSN-3-1', 'subject': 'NCM301', 'term': '2024-2025-1st', 'professor': 'prof_garcia', 'schedule': 'MWF 10:00-11:00 AM','room': 'NUR-301'},
    {'section_name': 'BSN-4-1', 'subject': 'NCM401', 'term': '2024-2025-1st', 'professor': 'prof_garcia', 'schedule': 'TTH 2:00-3:30 PM',  'room': 'NUR-401'},
    
    # BSN (Nursing) year1..4 (2nd sem)
    {'section_name': 'BSN-1-2', 'subject': 'NURS102', 'term': '2024-2025-2nd', 'professor': 'prof_santos', 'schedule': 'MWF 8:30-9:30 AM', 'room': 'NUR-102'},
    {'section_name': 'BSN-1-2', 'subject': 'BIO102', 'term': '2024-2025-2nd', 'professor': 'prof_garcia', 'schedule': 'TTH 9:30-11:00 AM', 'room': 'NUR-103'},
    {'section_name': 'BSN-2-2', 'subject': 'NCM202', 'term': '2024-2025-2nd', 'professor': 'prof_reyes',  'schedule': 'TTH 11:00-12:30 NN', 'room': 'NUR-202'},
    {'section_name': 'BSN-3-2', 'subject': 'NCM302', 'term': '2024-2025-2nd', 'professor': 'prof_garcia', 'schedule': 'MWF 1:00-2:00 PM', 'room': 'NUR-302'},
    {'section_name': 'BSN-4-2', 'subject': 'NCM402', 'term': '2024-2025-2nd', 'professor': 'prof_garcia', 'schedule': 'TTH 3:30-5:00 PM', 'room': 'NUR-402'},

    # BSCRIM (Criminology) year1..4 (1st sem)
    {'section_name': 'BSCRIM-1-1', 'subject': 'CRIM101', 'term': '2024-2025-1st', 'professor': 'prof_reyes',    'schedule': 'MWF 8:00-9:00 AM',  'room': 'CRIM-101'},
    {'section_name': 'BSCRIM-2-1', 'subject': 'CRIM201', 'term': '2024-2025-1st', 'professor': 'prof_garcia',   'schedule': 'TTH 10:00-11:30 AM','room': 'CRIM-201'},
    {'section_name': 'BSCRIM-3-1', 'subject': 'CRIM301', 'term': '2024-2025-1st', 'professor': 'prof_cenita',   'schedule': 'MWF 1:00-2:00 PM',  'room': 'CRIM-301'},
    {'section_name': 'BSCRIM-4-1', 'subject': 'CRIM401', 'term': '2024-2025-1st', 'professor': 'prof_orendain', 'schedule': 'TTH 3:00-4:30 PM',  'room': 'CRIM-401'},
    
    # BSCRIM (Criminology) year1..4 (2nd sem)
    {'section_name': 'BSCRIM-1-2', 'subject': 'CRIM102', 'term': '2024-2025-2nd', 'professor': 'prof_reyes',    'schedule': 'MWF 9:00-10:00 AM', 'room': 'CRIM-102'},
    {'section_name': 'BSCRIM-2-2', 'subject': 'LAW201', 'term': '2024-2025-2nd', 'professor': 'prof_orendain',  'schedule': 'TTH 11:30-1:00 PM', 'room': 'CRIM-202'},
    {'section_name': 'BSCRIM-3-2', 'subject': 'CRIM302', 'term': '2024-2025-2nd', 'professor': 'prof_cenita',   'schedule': 'MWF 2:00-3:00 PM', 'room': 'CRIM-302'},
    {'section_name': 'BSCRIM-3-2', 'subject': 'PSY302', 'term': '2024-2025-2nd', 'professor': 'prof_garcia',    'schedule': 'TTH 1:00-2:30 PM', 'room': 'CRIM-303'},
    {'section_name': 'BSCRIM-4-2', 'subject': 'PSY402', 'term': '2024-2025-2nd', 'professor': 'prof_garcia',    'schedule': 'TTH 4:30-6:00 PM', 'room': 'CRIM-402'},

    # BSTM (Tourism Management) year1..4 (1st sem)
    {'section_name': 'BSTM-1-1', 'subject': 'TM101', 'term': '2024-2025-1st', 'professor': 'prof_santos',    'schedule': 'MWF 7:30-8:30 AM',  'room': 'TM-101'},
    {'section_name': 'BSTM-2-1', 'subject': 'TM201', 'term': '2024-2025-1st', 'professor': 'prof_reyes',     'schedule': 'TTH 8:00-9:30 AM',  'room': 'TM-201'},
    {'section_name': 'BSTM-2-1', 'subject': 'HRM101', 'term': '2024-2025-1st', 'professor': 'prof_pangilinan', 'schedule': 'MWF 9:00-10:00 AM', 'room': 'TM-202'},
    {'section_name': 'BSTM-3-1', 'subject': 'TM301', 'term': '2024-2025-1st', 'professor': 'prof_garcia',    'schedule': 'MWF 9:30-10:30 AM', 'room': 'TM-301'},
    {'section_name': 'BSTM-3-1', 'subject': 'HRM301', 'term': '2024-2025-1st', 'professor': 'prof_pangilinan', 'schedule': 'TTH 10:00-11:30 AM', 'room': 'TM-302'},
    {'section_name': 'BSTM-4-1', 'subject': 'TM401', 'term': '2024-2025-1st', 'professor': 'prof_africa',    'schedule': 'TTH 1:00-2:30 PM',  'room': 'TM-401'},
    {'section_name': 'BSTM-4-1', 'subject': 'FIN401', 'term': '2024-2025-1st', 'professor': 'prof_orendain', 'schedule': 'MWF 1:00-2:00 PM',  'room': 'TM-402'},

    # BSTM (Tourism Management) year1..4 (2nd sem)
    {'section_name': 'BSTM-1-2', 'subject': 'TM102', 'term': '2024-2025-2nd', 'professor': 'prof_santos',     'schedule': 'MWF 8:30-9:30 AM',  'room': 'TM-102'},
    {'section_name': 'BSTM-2-2', 'subject': 'TM202', 'term': '2024-2025-2nd', 'professor': 'prof_reyes',      'schedule': 'TTH 9:30-11:00 AM', 'room': 'TM-202'},
    {'section_name': 'BSTM-2-2', 'subject': 'MKT101', 'term': '2024-2025-2nd', 'professor': 'prof_orendain',  'schedule': 'MWF 10:00-11:00 AM','room': 'TM-203'},
    {'section_name': 'BSTM-3-2', 'subject': 'TM302', 'term': '2024-2025-2nd', 'professor': 'prof_garcia',     'schedule': 'MWF 10:30-11:30 AM','room': 'TM-302'},
    {'section_name': 'BSTM-3-2', 'subject': 'HRM302', 'term': '2024-2025-2nd', 'professor': 'prof_pangilinan','schedule': 'TTH 11:30-1:00 PM', 'room': 'TM-303'},
    {'section_name': 'BSTM-4-2', 'subject': 'TM402', 'term': '2024-2025-2nd', 'professor': 'prof_africa',     'schedule': 'TTH 2:30-4:00 PM',  'room': 'TM-402'},

    # BSCE (Civil Engineering) year1..4 (1st sem)
    {'section_name': 'BSCE-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes',     'schedule': 'MWF 7:30-8:30 AM',  'room': 'CE-101'},
    {'section_name': 'BSCE-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos',     'schedule': 'TTH 8:00-9:30 AM',  'room': 'CE-102'},
    {'section_name': 'BSCE-1-1', 'subject': 'SELF101', 'term': '2024-2025-1st', 'professor': 'prof_garcia',    'schedule': 'MWF 9:00-10:00 AM', 'room': 'CE-103'},
    {'section_name': 'BSCE-1-1', 'subject': 'CE101', 'term': '2024-2025-1st', 'professor': 'prof_dela_cruz',   'schedule': 'TTH 10:00-11:30 AM','room': 'CE-104'},
    {'section_name': 'BSCE-2-1', 'subject': 'CE201', 'term': '2024-2025-1st', 'professor': 'prof_dela_cruz',   'schedule': 'MWF 10:00-11:00 AM','room': 'CE-201'},
    {'section_name': 'BSCE-3-1', 'subject': 'CE301', 'term': '2024-2025-1st', 'professor': 'prof_africa',      'schedule': 'MWF 2:00-3:00 PM',  'room': 'CE-301'},
    {'section_name': 'BSCE-4-1', 'subject': 'CE401', 'term': '2024-2025-1st', 'professor': 'prof_cenita',      'schedule': 'TTH 3:00-4:30 PM',  'room': 'CE-401'},

    # BSCE (Civil Engineering) year1..4 (2nd sem)
    {'section_name': 'BSCE-1-2', 'subject': 'MATH102', 'term': '2024-2025-2nd', 'professor': 'prof_reyes',     'schedule': 'MWF 8:00-9:00 AM',  'room': 'CE-105'},
    {'section_name': 'BSCE-1-2', 'subject': 'CHEM101', 'term': '2024-2025-2nd', 'professor': 'prof_garcia',    'schedule': 'TTH 9:00-10:30 AM', 'room': 'CE-106'},
    {'section_name': 'BSCE-1-2', 'subject': 'CE102', 'term': '2024-2025-2nd', 'professor': 'prof_dela_cruz',   'schedule': 'MWF 10:00-11:00 AM','room': 'CE-107'},
    {'section_name': 'BSCE-2-2', 'subject': 'CE202', 'term': '2024-2025-2nd', 'professor': 'prof_dela_cruz',   'schedule': 'TTH 11:00-12:30 NN','room': 'CE-202'},
    {'section_name': 'BSCE-3-2', 'subject': 'CE302', 'term': '2024-2025-2nd', 'professor': 'prof_africa',      'schedule': 'MWF 3:00-4:00 PM',  'room': 'CE-302'},
    {'section_name': 'BSCE-4-2', 'subject': 'CE402', 'term': '2024-2025-2nd', 'professor': 'prof_cenita',      'schedule': 'TTH 4:00-5:30 PM',  'room': 'CE-402'},

    # BSAIS (Accounting Information Systems) year1..4 (1st sem)
    {'section_name': 'BSAIS-1-1', 'subject': 'ACC101', 'term': '2024-2025-1st', 'professor': 'prof_orendain', 'schedule': 'MWF 8:00-9:00 AM',  'room': 'ACC-101'},
    {'section_name': 'BSAIS-2-1', 'subject': 'ACC201', 'term': '2024-2025-1st', 'professor': 'prof_delmonte', 'schedule': 'TTH 9:30-11:00 AM', 'room': 'ACC-201'},
    {'section_name': 'BSAIS-3-1', 'subject': 'ACC301', 'term': '2024-2025-1st', 'professor': 'prof_orendain', 'schedule': 'MWF 1:00-2:00 PM',  'room': 'ACC-301'},
    {'section_name': 'BSAIS-4-1', 'subject': 'AUD401', 'term': '2024-2025-1st', 'professor': 'prof_delmonte', 'schedule': 'TTH 2:00-3:30 PM',  'room': 'ACC-401'},
    {'section_name': 'BSAIS-4-1', 'subject': 'LAW401', 'term': '2024-2025-1st', 'professor': 'prof_reyes',    'schedule': 'MWF 3:00-4:00 PM',  'room': 'ACC-402'},

    # BSAIS (Accounting Information Systems) year1..4 (2nd sem)
    {'section_name': 'BSAIS-1-2', 'subject': 'ACC102', 'term': '2024-2025-2nd', 'professor': 'prof_orendain', 'schedule': 'MWF 9:00-10:00 AM', 'room': 'ACC-102'},
    {'section_name': 'BSAIS-2-2', 'subject': 'ACC202', 'term': '2024-2025-2nd', 'professor': 'prof_delmonte', 'schedule': 'TTH 11:00-12:30 NN','room': 'ACC-202'},
    {'section_name': 'BSAIS-3-2', 'subject': 'ACC302', 'term': '2024-2025-2nd', 'professor': 'prof_orendain', 'schedule': 'MWF 2:00-3:00 PM',  'room': 'ACC-302'},

    # BSEntrep (Entrepreneurship)
    {'section_name': 'BSEntrep-1-1', 'subject': 'ENT101', 'term': '2024-2025-1st', 'professor': 'prof_orendain', 'schedule': 'MWF 10:00-11:00 AM','room': 'ENT-101'},
    {'section_name': 'BSEntrep-2-1', 'subject': 'ENT201', 'term': '2024-2025-1st', 'professor': 'prof_africa',   'schedule': 'TTH 1:00-2:30 PM',  'room': 'ENT-201'},

    # BCED (Culture and Arts Education)
    {'section_name': 'BCED-1-1', 'subject': 'ART101', 'term': '2024-2025-1st', 'professor': 'prof_pangilinan', 'schedule': 'MWF 9:00-10:00 AM', 'room': 'ART-101'},
    {'section_name': 'BCED-2-1', 'subject': 'ART201', 'term': '2024-2025-1st', 'professor': 'prof_garcia',     'schedule': 'TTH 10:00-11:30 AM','room': 'ART-201'},

    # BTVTED (Tech-Vocational Teacher Ed)
    {'section_name': 'BTVTED-1-1', 'subject': 'TVT101', 'term': '2024-2025-1st', 'professor': 'prof_cenita', 'schedule': 'MWF 8:00-9:00 AM',  'room': 'TVT-101'},
    {'section_name': 'BTVTED-2-1', 'subject': 'TVT201', 'term': '2024-2025-1st', 'professor': 'prof_africa', 'schedule': 'TTH 9:00-10:30 AM', 'room': 'TVT-201'},

    # -------------------------------
    # 3-YEAR PROGRAMS
    # -------------------------------
    
    # TTHMT (Tourism & Hospitality Tech) year1..3 (1st sem)
    {'section_name': 'TTHMT-1-1', 'subject': 'TH101', 'term': '2024-2025-1st', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 7:30-8:30 AM',  'room': 'TH-101'},
    {'section_name': 'TTHMT-2-1', 'subject': 'TH201', 'term': '2024-2025-1st', 'professor': 'prof_santos',    'schedule': 'TTH 9:30-11:00 AM', 'room': 'TH-201'},
    {'section_name': 'TTHMT-3-1', 'subject': 'TH301', 'term': '2024-2025-1st', 'professor': 'prof_africa',    'schedule': 'MWF 11:00-12:00 NN','room': 'TH-301'},

    # TTHMT year1..3 (2nd sem)
    {'section_name': 'TTHMT-1-2', 'subject': 'TH102', 'term': '2024-2025-2nd', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 8:30-9:30 AM',  'room': 'TH-102'},
    {'section_name': 'TTHMT-2-2', 'subject': 'TH202', 'term': '2024-2025-2nd', 'professor': 'prof_santos',    'schedule': 'TTH 11:00-12:30 NN','room': 'TH-202'},
    {'section_name': 'TTHMT-3-2', 'subject': 'TH302', 'term': '2024-2025-2nd', 'professor': 'prof_africa',    'schedule': 'MWF 1:00-2:00 PM',  'room': 'TH-302'},

    # BFDIS (Business & Financial Data IS) year1..3 (1st sem)
    {'section_name': 'BFDIS-1-1', 'subject': 'BF101', 'term': '2024-2025-1st', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 8:30-9:30 AM',  'room': 'BF-101'},
    {'section_name': 'BFDIS-2-1', 'subject': 'BF201', 'term': '2024-2025-1st', 'professor': 'prof_orendain',  'schedule': 'TTH 1:00-2:30 PM',  'room': 'BF-201'},
    {'section_name': 'BFDIS-3-1', 'subject': 'BF301', 'term': '2024-2025-1st', 'professor': 'prof_delmonte',  'schedule': 'MWF 10:00-11:00 AM','room': 'BF-301'},

    # BFDIS year1..3 (2nd sem)
    {'section_name': 'BFDIS-1-2', 'subject': 'BF102', 'term': '2024-2025-2nd', 'professor': 'prof_dela_cruz', 'schedule': 'MWF 9:30-10:30 AM', 'room': 'BF-102'},
    {'section_name': 'BFDIS-2-2', 'subject': 'BF202', 'term': '2024-2025-2nd', 'professor': 'prof_orendain',  'schedule': 'TTH 2:30-4:00 PM',  'room': 'BF-202'},
    {'section_name': 'BFDIS-3-2', 'subject': 'BF302', 'term': '2024-2025-2nd', 'professor': 'prof_delmonte',  'schedule': 'MWF 11:00-12:00 NN','room': 'BF-302'},

    # -------------------------------
    # 2-YEAR PROGRAMS
    # -------------------------------

    # HRS (Hospitality & Restaurant Services) year1..2 (1st sem)
    {'section_name': 'HRS-1-1', 'subject': 'HRS101', 'term': '2024-2025-1st', 'professor': 'prof_dela_cruz',  'schedule': 'MWF 7:30-8:30 AM',  'room': 'HRS-101'},
    {'section_name': 'HRS-2-1', 'subject': 'HRS201', 'term': '2024-2025-1st', 'professor': 'prof_africa',     'schedule': 'TTH 9:30-11:00 AM', 'room': 'HRS-201'},

    # HRS year1..2 (2nd sem)
    {'section_name': 'HRS-1-2', 'subject':'HRS102', 'term': '2024-2025-2nd', 'professor': 'prof_dela_cruz',  'schedule': 'MWF 8:30-9:30 AM',  'room': 'HRS-102'},
    {'section_name': 'HRS-2-2', 'subject': 'HRS202', 'term': '2024-2025-2nd', 'professor': 'prof_africa',     'schedule': 'TTH 11:00-12:30 NN','room': 'HRS-202'},

    # CRS (Culinary & Restaurant Services) year1..2 (1st sem)
    {'section_name': 'CRS-1-1', 'subject': 'CRS101', 'term': '2024-2025-1st', 'professor': 'prof_garcia',     'schedule': 'MWF 8:30-9:30 AM',  'room': 'CRS-101'},
    {'section_name': 'CRS-2-1', 'subject': 'CRS201', 'term': '2024-2025-1st', 'professor': 'prof_cenita',     'schedule': 'TTH 10:30-12:00 NN','room': 'CRS-201'},

    # CRS year1..2 (2nd sem)
    {'section_name': 'CRS-1-2', 'subject': 'CRS102', 'term': '2024-2025-2nd', 'professor': 'prof_garcia',     'schedule': 'MWF 9:30-10:30 AM', 'room': 'CRS-102'},
    {'section_name': 'CRS-2-2', 'subject': 'CRS202', 'term': '2024-2025-2nd', 'professor': 'prof_cenita',     'schedule': 'TTH 1:00-2:30 PM',  'room': 'CRS-202'},

    # BOAT (Business Office & Accounting Tech) year1..2 (1st sem)
    {'section_name': 'BOAT-1-1', 'subject': 'BOA101', 'term': '2024-2025-1st', 'professor': 'prof_delmonte',  'schedule': 'MWF 9:30-10:30 AM', 'room': 'BOA-101'},
    {'section_name': 'BOAT-2-1', 'subject': 'BOA201', 'term': '2024-2025-1st', 'professor': 'prof_orendain',  'schedule': 'TTH 1:30-3:00 PM',  'room': 'BOA-201'},

    # BOAT year1..2 (2nd sem)
    {'section_name': 'BOAT-1-2', 'subject': 'BOA102', 'term': '2024-2025-2nd', 'professor': 'prof_delmonte',  'schedule': 'MWF 10:30-11:30 AM','room': 'BOA-102'},
    {'section_name': 'BOAT-2-2', 'subject': 'BOA202', 'term': '2024-2025-2nd', 'professor': 'prof_orendain',  'schedule': 'TTH 3:00-4:30 PM',  'room': 'BOA-202'},

    # SSWT (Salon, Spa & Wellness Tech) year1..2 (1st sem)
    {'section_name': 'SSWT-1-1', 'subject': 'SSW101', 'term': '2024-2025-1st', 'professor': 'prof_pangilinan','schedule': 'MWF 10:00-11:00 AM','room': 'SSW-101'},
    {'section_name': 'SSWT-2-1', 'subject': 'SSW201', 'term': '2024-2025-1st', 'professor': 'prof_pangilinan','schedule': 'TTH 2:00-3:30 PM',  'room': 'SSW-201'},

    # SSWT year1..2 (2nd sem)
    {'section_name': 'SSWT-1-2', 'subject': 'SSW102', 'term': '2024-2025-2nd', 'professor': 'prof_pangilinan','schedule': 'MWF 11:00-12:00 NN','room': 'SSW-102'},
    {'section_name': 'SSWT-2-2', 'subject': 'SSW202', 'term': '2024-2025-2nd', 'professor': 'prof_pangilinan','schedule': 'TTH 3:30-5:00 PM',  'room': 'SSW-202'},

    # ICT (2-year) year1..2 (1st sem)
    {'section_name': 'ICT-1-1', 'subject': 'ICT101', 'term': '2024-2025-1st', 'professor': 'prof_reyes',      'schedule': 'MWF 8:00-9:00 AM',  'room': 'ICT-101'},
    {'section_name': 'ICT-2-1', 'subject': 'ICT201', 'term': '2024-2025-1st', 'professor': 'prof_santos',     'schedule': 'TTH 9:30-11:00 AM', 'room': 'ICT-201'},

    # ICT year1..2 (2nd sem)
    {'section_name': 'ICT-1-2', 'subject': 'ICT102', 'term': '2024-2025-2nd', 'professor': 'prof_reyes',      'schedule': 'MWF 9:00-10:00 AM', 'room': 'ICT-102'},
    {'section_name': 'ICT-2-2', 'subject': 'ICT202', 'term': '2024-2025-2nd', 'professor': 'prof_santos',     'schedule': 'TTH 9:30-11:00 AM', 'room': 'ICT-201'},

    # General Education subjects that are shared across programs
    {'section_name': 'BSIS-3-1', 'subject': 'IS301-C', 'term': '2024-2025-1st', 'professor': 'prof_cenita',    'schedule': 'MWF 1:00-2:00 PM',  'room': 'CS-304'},
    {'section_name': 'BSIS-3-2', 'subject': 'IS302-C', 'term': '2024-2025-2nd', 'professor': 'prof_cenita',    'schedule': 'MWF 11:00-12:00 NN','room': 'CS-306'},
    {'section_name': 'BSTM-2-1', 'subject': 'HRM101', 'term': '2024-2025-1st', 'professor': 'prof_pangilinan', 'schedule': 'TTH 10:00-11:30 AM','room': 'TM-203'},
    {'section_name': 'BSTM-4-1', 'subject': 'FIN401', 'term': '2024-2025-1st', 'professor': 'prof_orendain',   'schedule': 'MWF 2:00-3:00 PM',  'room': 'TM-403'},
    {'section_name': 'BSTM-2-2', 'subject': 'MKT101', 'term': '2024-2025-2nd', 'professor': 'prof_orendain',   'schedule': 'TTH 1:00-2:30 PM',  'room': 'TM-204'},
    {'section_name': 'BSCRIM-1-1', 'subject': 'CRIM101', 'term': '2024-2025-1st', 'professor': 'prof_reyes',   'schedule': 'MWF 9:00-10:00 AM', 'room': 'CRIM-101'},
    {'section_name': 'BSCRIM-1-2', 'subject': 'CRIM102', 'term': '2024-2025-2nd', 'professor': 'prof_reyes',   'schedule': 'MWF 10:00-11:00 AM','room': 'CRIM-102'},
    {'section_name': 'BSCRIM-2-1', 'subject': 'CRIM201', 'term': '2024-2025-1st', 'professor': 'prof_garcia',  'schedule': 'TTH 9:00-10:30 AM', 'room': 'CRIM-201'},
    {'section_name': 'BSCRIM-2-2', 'subject': 'LAW201', 'term': '2024-2025-2nd', 'professor': 'prof_orendain', 'schedule': 'TTH 10:30-12:00 NN','room': 'CRIM-202'},
    {'section_name': 'BSCRIM-4-1', 'subject': 'CRIM401', 'term': '2024-2025-1st', 'professor': 'prof_cenita',  'schedule': 'MWF 2:00-3:00 PM',  'room': 'CRIM-401'},
    {'section_name': 'BSCRIM-4-2', 'subject': 'PSY402', 'term': '2024-2025-2nd', 'professor': 'prof_garcia',   'schedule': 'TTH 3:00-4:30 PM',  'room': 'CRIM-402'},
    {'section_name': 'BSN-1-1', 'subject': 'BIO101', 'term': '2024-2025-1st', 'professor': 'prof_garcia',      'schedule': 'TTH 10:00-11:30 AM','room': 'NUR-103'},
    {'section_name': 'BSAIS-2-1', 'subject': 'ACC201', 'term': '2024-2025-1st', 'professor': 'prof_delmonte',  'schedule': 'MWF 9:00-10:00 AM', 'room': 'ACC-201'},
    {'section_name': 'BSAIS-2-2', 'subject': 'ACC202', 'term': '2024-2025-2nd', 'professor': 'prof_delmonte',  'schedule': 'MWF 10:00-11:00 AM','room': 'ACC-202'},
    {'section_name': 'BSAIS-3-1', 'subject': 'ACC301', 'term': '2024-2025-1st', 'professor': 'prof_orendain',  'schedule': 'TTH 1:00-2:30 PM',  'room': 'ACC-301'},
    {'section_name': 'BSAIS-3-2', 'subject': 'ACC302', 'term': '2024-2025-2nd', 'professor': 'prof_orendain',  'schedule': 'TTH 2:30-4:00 PM',  'room': 'ACC-302'},
    {'section_name': 'BSAIS-4-1', 'subject': 'AUD401', 'term': '2024-2025-1st', 'professor': 'prof_delmonte',  'schedule': 'MWF 1:00-2:00 PM',  'room': 'ACC-401'},
    {'section_name': 'BSAIS-4-1', 'subject': 'LAW401', 'term': '2024-2025-1st', 'professor': 'prof_reyes',     'schedule': 'TTH 3:00-4:30 PM',  'room': 'ACC-402'},

    {'section_name': 'BSIS-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 7:30-9:00 AM', 'room': 'LIB-101'},
    {'section_name': 'BSN-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 1:00-2:30 PM', 'room': 'LIB-102'},

    {'section_name': 'BSAIS-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 11:00-12:00 NN', 'room': 'LIB-103'},
    {'section_name': 'BSEntrep-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 1:00-2:00 PM', 'room': 'LIB-104'},
    {'section_name': 'BCED-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 9:00-10:30 AM', 'room': 'LIB-105'},
    {'section_name': 'BTVTED-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 10:30-12:00 NN', 'room': 'LIB-106'},
    {'section_name': 'TTHMT-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 2:00-3:00 PM', 'room': 'LIB-107'},
    {'section_name': 'BFDIS-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 3:00-4:00 PM', 'room': 'LIB-108'},
    {'section_name': 'HRS-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 2:30-4:00 PM', 'room': 'LIB-109'},
    {'section_name': 'CRS-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 4:00-5:30 PM', 'room': 'LIB-110'},
    {'section_name': 'BOAT-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 4:00-5:00 PM', 'room': 'LIB-111'},
    {'section_name': 'SSWT-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 5:00-6:00 PM', 'room': 'LIB-112'},
    {'section_name': 'ICT-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 4:30-6:00 PM', 'room': 'LIB-113'},
    {'section_name': 'BSCRIM-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 10:00-11:00 AM', 'room': 'LIB-114'},
    {'section_name': 'BSTM-1-1', 'subject': 'MATH101', 'term': '2024-2025-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 7:00-8:30 AM', 'room': 'LIB-115'},

    
    {'section_name': 'BSCE-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'TTH 8:00-9:30 AM', 'room': 'CE-102'},
    {'section_name': 'BSIS-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'MWF 7:00-8:00 AM', 'room': 'LIB-201'},
    {'section_name': 'BSN-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'MWF 1:00-2:00 PM', 'room': 'LIB-202'},
    {'section_name': 'BSAIS-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'TTH 11:30-1:00 PM', 'room': 'LIB-203'},
    {'section_name': 'BSCRIM-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'TTH 1:00-2:30 PM', 'room': 'LIB-204'},
    {'section_name': 'BSTM-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'TTH 2:30-4:00 PM', 'room': 'LIB-205'},
    {'section_name': 'ICT-1-1', 'subject': 'ENG101', 'term': '2024-2025-1st', 'professor': 'prof_santos', 'schedule': 'MWF 2:00-3:00 PM', 'room': 'LIB-206'},
 
    {'section_name': 'BSIS-3-1', 'subject': 'MATH301', 'term': '2022-2023-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 10:00-11:00 AM', 'room': 'GEN-002'},
    
    {'section_name': 'BSIS-2-1', 'subject': 'MATH201', 'term': '2023-2024-1st', 'professor': 'prof_reyes', 'schedule': 'MWF 10:00-11:00 AM', 'room': 'GEN-001'},
    {'section_name': 'BSAIS-2-1', 'subject': 'MATH201', 'term': '2023-2024-1st', 'professor': 'prof_reyes', 'schedule': 'TTH 8:00-9:30 AM', 'room': 'GEN-005'},

    {'section_name': 'BSAIS-2-1', 'subject': 'ECON201', 'term': '2023-2024-1st', 'professor': 'prof_orendain', 'schedule': 'TTH 10:30-12:00 NN', 'room': 'ACC-001'},
    

]

sections = {}
for data in sections_data:
    prof_user = users.get(data['professor'])
    if not prof_user:
        print(f"  ⚠️  Skipping section for {data['subject']}: professor {data['professor']} not found")
        continue

    section, created = Section.objects.get_or_create(
        section_name=data['section_name'],  
        subject=subjects[data['subject']],
        term=data['term'], 
        schedule=data['schedule'],
        defaults={
            'professor': prof_user,
            'room': data['room']
        }
    )
    

    section_key = f"{data['section_name']}-{data['subject']}"
    sections[section_key] = section
    
    status = "✅ Created" if created else "⏭️  Exists"
    prof_name = prof_user.get_full_name()
    print(f"  {status}: {data['section_name']} - {data['subject']} - {data['term']} - {data['schedule']} ({data['room']}) - Prof. {prof_name}")

print(f"\n✅ Total Sections: {len(sections)}\n")

# ========================================
# 6. SAMPLE ENROLLMENTS
# ========================================

enrollments_data = [
       # Student Kirt (2021-00001) - BSIS, Year 3
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'IS301-A', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'MATH301', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'IS301-B', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'IS301-C', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00001', 'section': 'BSIS-2-2', 'subject': 'IS202-A', 'term': '2nd', 'status': 'completed'},
    {'student': '2021-00001', 'section': 'BSIS-2-1', 'subject': 'IS201-B', 'term': '1st', 'status': 'completed'},

    # Student Anna (2022-00003) - BSAIS, Year 2
    {'student': '2022-00003', 'section': 'BSAIS-2-1', 'subject': 'ACC201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00003', 'section': 'BSAIS-2-1', 'subject': 'ECON201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00003', 'section': 'BSAIS-1-2', 'subject': 'ACC102', 'term': '2nd', 'status': 'completed'},

    # Student Pedro (2023-00004) - ICT, Year 1
    {'student': '2023-00004', 'section': 'ICT-1-1', 'subject': 'ICT101', 'term': '1st', 'status': 'enrolled'},

    # Student Ian (2021-00008) - BSTM, Year 4
    {'student': '2021-00008', 'section': 'BSTM-4-1', 'subject': 'FIN401', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00008', 'section': 'BSTM-3-2', 'subject': 'TM302', 'term': '2nd', 'status': 'completed'},
    {'student': '2021-00008', 'section': 'BSTM-3-2', 'subject': 'HRM302', 'term': '2nd', 'status': 'completed'},

    # Student Marie (2021-00009) - BSN, Year 4
    {'student': '2021-00009', 'section': 'BSN-4-1', 'subject': 'NCM401', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00009', 'section': 'BSN-3-2', 'subject': 'NCM302', 'term': '2nd', 'status': 'completed'},

    # Student Jason (2023-00016) - BSN, Year 1
    {'student': '2023-00016', 'section': 'BSN-1-1', 'subject': 'NURS101', 'term': '1st', 'status': 'enrolled'},
    {'student': '2023-00016', 'section': 'BSN-1-1', 'subject': 'BIO101', 'term': '1st', 'status': 'enrolled'},

    # Student Carlo (2022-00018) - BSIS, Year 2
    {'student': '2022-00018', 'section': 'BSIS-2-1', 'subject': 'IS201-A', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00018', 'section': 'BSIS-2-1', 'subject': 'IS201-B', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00018', 'section': 'BSIS-1-2', 'subject': 'IS102-A', 'term': '2nd', 'status': 'completed'},

    # Student Jun (2021-00002) - BSIS, Year 3
    {'student': '2021-00002', 'section': 'BSIS-3-1', 'subject': 'IS301-A', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00002', 'section': 'BSIS-3-1', 'subject': 'MATH301', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00002', 'section': 'BSIS-3-1', 'subject': 'IS301-B', 'term': '1st', 'status': 'enrolled'},

    # Student Joyce (2022-00007) - BSAIS, Year 2
    {'student': '2022-00007', 'section': 'BSAIS-2-1', 'subject': 'ACC201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00007', 'section': 'BSAIS-2-1', 'subject': 'ECON201', 'term': '1st', 'status': 'enrolled'},

    # Student Kyle (2023-00010) - BSIS, Year 1
    {'student': '2023-00010', 'section': 'BSIS-1-1', 'subject': 'IS101-A', 'term': '1st', 'status': 'enrolled'},
    {'student': '2023-00010', 'section': 'BSIS-1-1', 'subject': 'IS101-B', 'term': '1st', 'status': 'enrolled'},

    # Student Sophia (2022-00011) - BSAIS, Year 2
    {'student': '2022-00011', 'section': 'BSAIS-2-1', 'subject': 'ACC201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00011', 'section': 'BSAIS-2-1', 'subject': 'ECON201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00011', 'section': 'BSAIS-1-2', 'subject': 'ACC102', 'term': '2nd', 'status': 'completed'},

    # Student Josh (2021-00012) - ICT, Year 3
    {'student': '2021-00012', 'section': 'ICT-2-2', 'subject': 'ICT202', 'term': '2nd', 'status': 'enrolled'},
    {'student': '2021-00012', 'section': 'ICT-2-1', 'subject': 'ICT201', 'term': '1st', 'status': 'completed'},

    # Student Megan (2022-00013) - BSCRIM, Year 2
    {'student': '2022-00013', 'section': 'BSCRIM-2-1', 'subject': 'CRIM201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00013', 'section': 'BSCRIM-1-2', 'subject': 'CRIM102', 'term': '2nd', 'status': 'completed'},

    # Student Matt (2023-00014) - BSIS, Year 1
    {'student': '2023-00014', 'section': 'BSIS-1-1', 'subject': 'IS101-A', 'term': '1st', 'status': 'enrolled'},
    {'student': '2023-00014', 'section': 'BSIS-1-1', 'subject': 'IS101-B', 'term': '1st', 'status': 'enrolled'},

    # Student Grace (2021-00017) - BSCRIM, Year 4
    {'student': '2021-00017', 'section': 'BSCRIM-4-1', 'subject': 'CRIM401', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00017', 'section': 'BSCRIM-3-2', 'subject': 'CRIM302', 'term': '2nd', 'status': 'completed'},

    # Student Paul (2021-00020) - BSAIS, Year 4
    {'student': '2021-00020', 'section': 'BSAIS-4-1', 'subject': 'AUD401', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00020', 'section': 'BSAIS-4-1', 'subject': 'LAW401', 'term': '1st', 'status': 'enrolled'},
    {'student': '2021-00020', 'section': 'BSAIS-3-2', 'subject': 'ACC302', 'term': '2nd', 'status': 'completed'},

    # Student Lisa (2022-00005) - BSTM, Year 2
    {'student': '2022-00005', 'section': 'BSTM-2-1', 'subject': 'TM201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00005', 'section': 'BSTM-2-1', 'subject': 'HRM101', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00005', 'section': 'BSTM-1-2', 'subject': 'TM102', 'term': '2nd', 'status': 'completed'},

    # Student Rafael (2023-00006) - BSCRIM, Year 1
    {'student': '2023-00006', 'section': 'BSCRIM-1-1', 'subject': 'CRIM101', 'term': '1st', 'status': 'enrolled'},

    # Student Ella (2022-00015) - BSTM, Year 2
    {'student': '2022-00015', 'section': 'BSTM-2-1', 'subject': 'TM201', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00015', 'section': 'BSTM-2-1', 'subject': 'HRM101', 'term': '1st', 'status': 'enrolled'},
    {'student': '2022-00015', 'section': 'BSTM-1-1', 'subject': 'TM101', 'term': '1st', 'status': 'completed'},

    # Student Nina (2023-00019) - BSTM, Year 1
    {'student': '2023-00019', 'section': 'BSTM-1-1', 'subject': 'TM101', 'term': '1st', 'status': 'enrolled'},
]

for data in enrollments_data:
    # Build the section key to match how sections are stored
    section_key = f"{data['section']}-{data['subject']}"
    
    if section_key in sections and data['student'] in students:
        enrollment, created = Enrollment.objects.get_or_create(
            student=students[data['student']],
            section=sections[section_key],  # ✅ Use the correct key
            term=data['term'],  # ✅ Use term from data, not hardcoded
            defaults={'status': data['status']}
        )
        status = "✅ Created" if created else "⏭️  Exists"
        student_name = students[data['student']].user.get_full_name()
        print(f"  {status}: {student_name} enrolled in {data['section']} - {data['subject']} ({data['term']})")
    else:
        print(f"  ⚠️  Skipping enrollment: missing section or student for {data}")

print()

# ========================================
# 8. SAMPLE GRADES (with Section)
# ========================================
print("📊 Creating Sample Grades...")

grades_data = [
    # Student Kirt (2021-00001) - BSIS, Year 3
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'IS301-A', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'MATH301', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'IS301-B', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00001', 'section': 'BSIS-3-1', 'subject': 'IS301-C', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00001', 'section': 'BSIS-2-2', 'subject': 'IS202-A', 'grade': 1.75, 'status': 'passed'},
    {'student': '2021-00001', 'section': 'BSIS-2-1', 'subject': 'IS201-B', 'grade': 2.0, 'status': 'passed'},

    # Student Anna (2022-00003) - BSAIS, Year 2
    {'student': '2022-00003', 'section': 'BSAIS-2-1', 'subject': 'ACC201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00003', 'section': 'BSAIS-2-1', 'subject': 'ECON201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00003', 'section': 'BSAIS-1-2', 'subject': 'ACC102', 'grade': 1.5, 'status': 'passed'},

    # Student Pedro (2023-00004) - ICT, Year 1
    {'student': '2023-00004', 'section': 'ICT-1-1', 'subject': 'ICT101', 'grade': None, 'status': 'ongoing'},

    # Student Ian (2021-00008) - BSTM, Year 4
    {'student': '2021-00008', 'section': 'BSTM-4-1', 'subject': 'FIN401', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00008', 'section': 'BSTM-3-2', 'subject': 'TM302', 'grade': 1.5, 'status': 'passed'},
    {'student': '2021-00008', 'section': 'BSTM-3-2', 'subject': 'HRM302', 'grade': 1.25, 'status': 'passed'},

    # Student Marie (2021-00009) - BSN, Year 4
    {'student': '2021-00009', 'section': 'BSN-4-1', 'subject': 'NCM401', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00009', 'section': 'BSN-3-2', 'subject': 'NCM302', 'grade': 2.5, 'status': 'passed'},

    # Student Jason (2023-00016) - BSN, Year 1
    {'student': '2023-00016', 'section': 'BSN-1-1', 'subject': 'NURS101', 'grade': None, 'status': 'ongoing'},
    {'student': '2023-00016', 'section': 'BSN-1-1', 'subject': 'BIO101', 'grade': None, 'status': 'ongoing'},

    # Student Carlo (2022-00018) - BSIS, Year 2
    {'student': '2022-00018', 'section': 'BSIS-2-1', 'subject': 'IS201-A', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00018', 'section': 'BSIS-2-1', 'subject': 'IS201-B', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00018', 'section': 'BSIS-1-2', 'subject': 'IS102-A', 'grade': 2.0, 'status': 'passed'},

    # Student Jun (2021-00002) - BSIS, Year 3
    {'student': '2021-00002', 'section': 'BSIS-3-1', 'subject': 'IS301-A', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00002', 'section': 'BSIS-3-1', 'subject': 'MATH301', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00002', 'section': 'BSIS-3-1', 'subject': 'IS301-B', 'grade': None, 'status': 'ongoing'},

    # Student Joyce (2022-00007) - BSAIS, Year 2
    {'student': '2022-00007', 'section': 'BSAIS-2-1', 'subject': 'ACC201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00007', 'section': 'BSAIS-2-1', 'subject': 'ECON201', 'grade': None, 'status': 'ongoing'},

    # Student Kyle (2023-00010) - BSIS, Year 1
    {'student': '2023-00010', 'section': 'BSIS-1-1', 'subject': 'IS101-A', 'grade': None, 'status': 'ongoing'},
    {'student': '2023-00010', 'section': 'BSIS-1-1', 'subject': 'IS101-B', 'grade': None, 'status': 'ongoing'},

    # Student Sophia (2022-00011) - BSAIS, Year 2
    {'student': '2022-00011', 'section': 'BSAIS-2-1', 'subject': 'ACC201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00011', 'section': 'BSAIS-2-1', 'subject': 'ECON201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00011', 'section': 'BSAIS-1-2', 'subject': 'ACC102', 'grade': 2.0, 'status': 'passed'},

    # Student Josh (2021-00012) - ICT, Year 3
    {'student': '2021-00012', 'section': 'ICT-2-2', 'subject': 'ICT202', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00012', 'section': 'ICT-2-1', 'subject': 'ICT201', 'grade': 2.5, 'status': 'passed'},

    # Student Megan (2022-00013) - BSCRIM, Year 2
    {'student': '2022-00013', 'section': 'BSCRIM-2-1', 'subject': 'CRIM201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00013', 'section': 'BSCRIM-1-2', 'subject': 'CRIM102', 'grade': 1.75, 'status': 'passed'},

    # Student Matt (2023-00014) - BSIS, Year 1
    {'student': '2023-00014', 'section': 'BSIS-1-1', 'subject': 'IS101-A', 'grade': None, 'status': 'ongoing'},
    {'student': '2023-00014', 'section': 'BSIS-1-1', 'subject': 'IS101-B', 'grade': None, 'status': 'ongoing'},

    # Student Grace (2021-00017) - BSCRIM, Year 4
    {'student': '2021-00017', 'section': 'BSCRIM-4-1', 'subject': 'CRIM401', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00017', 'section': 'BSCRIM-3-2', 'subject': 'CRIM302', 'grade': 1.0, 'status': 'passed'},

    # Student Paul (2021-00020) - BSAIS, Year 4
    {'student': '2021-00020', 'section': 'BSAIS-4-1', 'subject': 'AUD401', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00020', 'section': 'BSAIS-4-1', 'subject': 'LAW401', 'grade': None, 'status': 'ongoing'},
    {'student': '2021-00020', 'section': 'BSAIS-3-2', 'subject': 'ACC302', 'grade': 1.25, 'status': 'passed'},

    # Student Lisa (2022-00005) - BSTM, Year 2
    {'student': '2022-00005', 'section': 'BSTM-2-1', 'subject': 'TM201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00005', 'section': 'BSTM-2-1', 'subject': 'HRM101', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00005', 'section': 'BSTM-1-2', 'subject': 'TM102', 'grade': 2.75, 'status': 'passed'},

    # Student Rafael (2023-00006) - BSCRIM, Year 1
    {'student': '2023-00006', 'section': 'BSCRIM-1-1', 'subject': 'CRIM101', 'grade': None, 'status': 'ongoing'},

    # Student Ella (2022-00015) - BSTM, Year 2
    {'student': '2022-00015', 'section': 'BSTM-2-1', 'subject': 'TM201', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00015', 'section': 'BSTM-2-1', 'subject': 'HRM101', 'grade': None, 'status': 'ongoing'},
    {'student': '2022-00015', 'section': 'BSTM-1-1', 'subject': 'TM101', 'grade': 2.25, 'status': 'passed'},

    # Student Nina (2023-00019) - BSTM, Year 1
    {'student': '2023-00019', 'section': 'BSTM-1-1', 'subject': 'TM101', 'grade': None, 'status': 'ongoing'},
]

for data in grades_data:
    section_key = f"{data['section']}-{data['subject']}"
    
    if section_key in sections and data['student'] in students:
        grade, created = Grade.objects.get_or_create(
            student=students[data['student']],
            subject=subjects[data['subject']],
            section=sections[section_key],
            defaults={
                'grade': data['grade'],
                'status': data['status'],
                'encoded_by': users.get('prof_dela_cruz')
            }
        )
        status = "✅ Created" if created else "⏭️  Exists"
        student_name = students[data['student']].user.get_full_name()
        print(f"  {status}: {student_name} - {data['subject']}: {data['grade']}")
    else:
        print(f"  ⚠️  Skipping grade for {data}")

print()

# ========================================
# SUMMARY
# ========================================
print("=" * 60)
print("✅ DATABASE SEEDING COMPLETED!")
print("=" * 60)
print(f"📚 Programs: {Program.objects.count()}")
print(f"👥 Users: {User.objects.count()}")
print(f"🎓 Students: {Student.objects.count()}")
print(f"📋 Curriculums: {Curriculum.objects.count()}")
print(f"📖 Subjects: {Subject.objects.count()}")
print(f"🏫 Sections: {Section.objects.count()}")
print(f"📝 Enrollments: {Enrollment.objects.count()}")
print(f"📊 Grades: {Grade.objects.count()}")
print("=" * 60)
print("\n🔐 Login Credentials (DEV):")
print("   Username: admin | Password:", PRINT_PASSWORD)
print("   Username: registrar1 | Password:", PRINT_PASSWORD)
print("   Username: student_kirt | Password:", PRINT_PASSWORD)
print("\n🚀 Run: python manage.py runserver")
print("   Then visit: http://127.0.0.1:8000/admin")
print("=" * 60)
