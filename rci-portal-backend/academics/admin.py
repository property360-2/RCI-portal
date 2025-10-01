from django.contrib import admin
from .models import (
    User, Program, Curriculum, Subject, Section,
    Student, Enrollment, Grade, Application, Document, AuditLog
)

# Register your models here.

admin.site.register(User)
admin.site.register(Program)
admin.site.register(Curriculum)
admin.site.register(Subject)
admin.site.register(Section)
admin.site.register(Student)
admin.site.register(Enrollment)
admin.site.register(Grade)
admin.site.register(Application)
admin.site.register(Document)
admin.site.register(AuditLog)
