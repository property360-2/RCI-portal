from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from .models import Student, AuditLog

User = get_user_model()

@receiver(post_save, sender=Student)
def log_student_save(sender, instance, created, **kwargs):
    AuditLog.objects.create(
        entity="Student",
        action="create" if created else "update",
        user=getattr(instance, "_changed_by", None),  # This is now set in admin
        details={
            "student_number": instance.student_number,
            "year_level": instance.year_level,
            "program": str(instance.program),
            "status": instance.status,
        }
    )

@receiver(post_delete, sender=Student)
def log_student_delete(sender, instance, **kwargs):
    AuditLog.objects.create(
        entity="Student",
        action="delete",
        user=getattr(instance, "_changed_by", None),
        details={
            "student_number": instance.student_number,
            "year_level": instance.year_level,
        }
    )
