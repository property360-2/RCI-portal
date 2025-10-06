import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rci_portal.settings")
django.setup()

# Import models only after Django is ready
from academics.models import Student, Grade

print("\n📊 All Students and Grades\n")

for student in Student.objects.all():
    print(f"\n🎓 {student.user.get_full_name()} ({student.student_id})")

    grades = Grade.objects.filter(student=student)
    if grades.exists():
        for g in grades:
            print(f"  • {g.subject.code} - {g.grade} ({g.status})")
    else:
        print("  ⚠️ No grades found")
