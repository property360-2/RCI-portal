# academics/admin.py

from django.contrib import admin
from django.utils.html import format_html
import json
from .models import (
    User, Program, Curriculum, Subject, Section,
    Student, Enrollment, Grade, Application, Document, AuditLog
)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    """
    Enhanced AuditLog admin with formatted details display
    """
    list_display = ['timestamp', 'action_colored', 'entity', 'user_display', 'details_preview']
    list_filter = ['action', 'entity', 'timestamp']
    search_fields = ['entity', 'user__username', 'user__email']
    readonly_fields = ['log_id', 'entity', 'action', 'user', 'details_formatted', 'timestamp']
    ordering = ['-timestamp']
    date_hierarchy = 'timestamp'
    
    def has_add_permission(self, request):
        return False
    
    def has_change_permission(self, request, obj=None):
        return False
    
    def has_delete_permission(self, request, obj=None):
        return request.user.is_superuser
    
    def action_colored(self, obj):
        """Display action with color coding"""
        colors = {
            'create': 'green',
            'update': 'orange',
            'delete': 'red',
        }
        color = colors.get(obj.action, 'gray')
        return format_html(
            '<span style="color: {}; font-weight: bold;">{}</span>',
            color,
            obj.get_action_display().upper()
        )
    action_colored.short_description = 'Action'
    
    def user_display(self, obj):
        """Display user with role"""
        if obj.user:
            return format_html(
                '<strong>{}</strong><br><small style="color: gray;">{}</small>',
                obj.user.username,
                obj.user.get_role_display()
            )
        return format_html('<em style="color: gray;">System</em>')
    user_display.short_description = 'User'
    
    def details_preview(self, obj):
        """Short preview of details for list view"""
        if not obj.details:
            return '-'
        
        try:
            details = obj.details
            if isinstance(details, str):
                details = json.loads(details)
            
            if obj.action == 'create':
                data = details.get('created_data', details)
                preview = []
                for key in ['student_number', 'username', 'code', 'program_code', 'title', 'name']:
                    if key in data:
                        preview.append(f"{key}: {data[key]}")
                return ', '.join(preview[:3]) if preview else 'Created'
            
            elif obj.action == 'update':
                changes = details.get('changes', {})
                if changes:
                    num_changes = len(changes)
                    field_names = ', '.join(list(changes.keys())[:3])
                    more = f" (+{num_changes - 3} more)" if num_changes > 3 else ""
                    return f"Changed: {field_names}{more}"
                # If no 'changes' key, show field names from direct data
                field_names = ', '.join(list(details.keys())[:3])
                more = f" (+{len(details) - 3} more)" if len(details) > 3 else ""
                return f"Updated: {field_names}{more}"
            
            elif obj.action == 'delete':
                if 'deleted_id' in details:
                    return f"Deleted ID: {details['deleted_id']}"
                return 'Deleted'
            
            return '-'
        except:
            return 'View details →'
    details_preview.short_description = 'Details'
    
    def details_formatted(self, obj):
        """Beautifully formatted details for detail view"""
        if not obj.details:
            return format_html('<em style="color: gray;">No details recorded</em>')
        
        from django.utils.safestring import mark_safe
        
        try:
            details = obj.details
            if isinstance(details, str):
                details = json.loads(details)
            
            # Try to get student info if student_number exists in details
            student_info = None
            if 'student_number' in details and obj.entity == 'Student':
                try:
                    from .models import Student
                    student = Student.objects.select_related('user').get(student_number=details['student_number'])
                    student_info = {
                        'name': student.user.get_full_name(),
                        'email': student.user.email,
                        'username': student.user.username
                    }
                except Student.DoesNotExist:
                    pass
            
            # Build HTML with improved styling
            html_parts = ['<div style="background: #ffffff; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">']
            
            # Show student info if available
            if student_info:
                html_parts.append('''
                    <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                padding: 20px; 
                                margin-bottom: 20px; 
                                border-radius: 8px; 
                                color: white;
                                box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
                        <h3 style="margin: 0 0 15px 0; font-size: 18px; font-weight: 600;">
                            👤 Student Information
                        </h3>
                        <div style="display: grid; gap: 8px;">
                ''')
                html_parts.append(f'''
                            <div style="background: rgba(255,255,255,0.1); padding: 10px; border-radius: 4px;">
                                <strong style="display: inline-block; width: 140px;">Name:</strong>
                                <span style="font-size: 16px;">{student_info["name"]}</span>
                            </div>
                            <div style="background: rgba(255,255,255,0.1); padding: 10px; border-radius: 4px;">
                                <strong style="display: inline-block; width: 140px;">Student Number:</strong>
                                <span style="font-size: 16px;">{details["student_number"]}</span>
                            </div>
                            <div style="background: rgba(255,255,255,0.1); padding: 10px; border-radius: 4px;">
                                <strong style="display: inline-block; width: 140px;">Email:</strong>
                                <span style="font-size: 16px;">{student_info["email"]}</span>
                            </div>
                ''')
                html_parts.append('</div></div>')
            
            # Show change details with better formatting
            html_parts.append('''
                <h3 style="margin: 0 0 15px 0; 
                        color: #333; 
                        font-size: 16px; 
                        font-weight: 600;
                        padding-bottom: 10px;
                        border-bottom: 2px solid #e0e0e0;">
                    📝 Change Details
                </h3>
            ''')
            
            json_str = json.dumps(details, indent=2)
            html_parts.append(f'''
                <pre style="background: #f8f9fa; 
                        padding: 20px; 
                        overflow-x: auto; 
                        border: 1px solid #e0e0e0;
                        border-radius: 6px;
                        margin: 0;
                        font-family: 'Consolas', 'Monaco', 'Courier New', monospace;
                        font-size: 13px;
                        line-height: 1.6;
                        color: #2d3748;">{json_str}</pre>
            ''')
            html_parts.append('</div>')
            
            return mark_safe(''.join(html_parts))
            
        except Exception as e:
            return format_html(
                '<div style="color: red;">Error: {}</div><pre>{}</pre>',
                str(e),
                repr(obj.details)
            )
    
    details_formatted.short_description = 'Detailed Information'
    
    def _format_value(self, value):
        """Format a value for display"""
        if value is None:
            return format_html('<em style="color: gray;">None</em>')
        if isinstance(value, bool):
            return '✓' if value else '✗'
        if isinstance(value, (list, dict)):
            # Don't use format_html for JSON - mark it as safe directly
            from django.utils.safestring import mark_safe
            json_str = json.dumps(value, indent=2)
            # Escape HTML manually
            json_str = json_str.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            return mark_safe(f'<pre style="margin: 0; background: #f9f9f9; padding: 5px;">{json_str}</pre>')
        # For regular strings, use format_html
        return format_html('{}', str(value))
    
    def _render_table(self, data, bg_color='#f0f0f0'):
        """Render a simple data table"""
        if not isinstance(data, dict):
            return ''
        
        from django.utils.safestring import mark_safe
        
        html = ['<table style="width: 100%; border-collapse: collapse;">']
        html.append(f'<tr style="background: {bg_color};"><th style="text-align: left; padding: 8px; border: 1px solid #ddd;">Field</th><th style="text-align: left; padding: 8px; border: 1px solid #ddd;">Value</th></tr>')
        
        for key, value in data.items():
            if key not in ['password', 'password_hash']:
                formatted_value = self._format_value(value)
                # Escape the key
                safe_key = format_html('{}', key)
                html.append(f'<tr><td style="padding: 8px; border: 1px solid #ddd;"><strong>{safe_key}</strong></td><td style="padding: 8px; border: 1px solid #ddd;">{formatted_value}</td></tr>')
        
        html.append('</table>')
        return mark_safe(''.join(html))
    
    def _render_changes_table(self, changes):
        """Render changes table with before/after"""
        if not isinstance(changes, dict):
            return ''
        
        from django.utils.safestring import mark_safe
        
        html = ['<table style="width: 100%; border-collapse: collapse;">']
        html.append('<tr style="background: #fff3e0;"><th style="text-align: left; padding: 8px; border: 1px solid #ddd;">Field</th><th style="text-align: left; padding: 8px; border: 1px solid #ddd;">Before</th><th style="text-align: left; padding: 8px; border: 1px solid #ddd;">After</th></tr>')
        
        for field, change in changes.items():
            before = self._format_value(change.get('before'))
            after = self._format_value(change.get('after'))
            safe_field = format_html('{}', field)
            html.append(f'<tr><td style="padding: 8px; border: 1px solid #ddd;"><strong>{safe_field}</strong></td><td style="padding: 8px; border: 1px solid #ddd; background: #ffebee;">{before}</td><td style="padding: 8px; border: 1px solid #ddd; background: #e8f5e9;">{after}</td></tr>')
        
        html.append('</table>')
        return mark_safe(''.join(html))


# ========================================
# ENHANCED USER ADMIN
# ========================================

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'role', 'full_name', 'is_active', 'date_joined']
    list_filter = ['role', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    readonly_fields = ['user_id', 'date_joined', 'last_login']
    ordering = ['-date_joined']
    
    fieldsets = (
        ('Account Info', {
            'fields': ('user_id', 'username', 'email', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name')
        }),
        ('Permissions', {
            'fields': ('role', 'is_active', 'is_staff', 'is_superuser')
        }),
        ('Dates', {
            'fields': ('date_joined', 'last_login')
        }),
    )
    
    def full_name(self, obj):
        return obj.get_full_name() or '-'
    full_name.short_description = 'Full Name'


# ========================================
# ENHANCED STUDENT ADMIN
# ========================================

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['student_number', 'full_name', 'program', 'year_level', 'status']
    list_filter = ['status', 'year_level', 'program']
    search_fields = ['student_number', 'user__username', 'user__first_name', 'user__last_name']
    readonly_fields = ['student_id']
    
    def full_name(self, obj):
        return obj.user.get_full_name()
    full_name.short_description = 'Name'


# ========================================
# ENHANCED GRADE ADMIN
# ========================================

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ['student_display', 'subject', 'grade', 'status', 'encoded_by', 'signatories_status']
    list_filter = ['status', 'section__term']
    search_fields = ['student__student_number', 'student__user__first_name', 'subject__code']
    readonly_fields = ['grade_id']
    
    def student_display(self, obj):
        return f"{obj.student.student_number} - {obj.student.user.get_full_name()}"
    student_display.short_description = 'Student'
    
    def signatories_status(self, obj):
        if obj.signatories:
            count = len(obj.signatories)
            return format_html('<span style="color: green;">✓ {} signatures</span>', count)
        return format_html('<span style="color: gray;">No signatures</span>')
    signatories_status.short_description = 'Signatures'


# ========================================
# REGISTER OTHER MODELS
# ========================================

@admin.register(Program)
class ProgramAdmin(admin.ModelAdmin):
    list_display = ['program_code', 'program_name', 'department', 'sector']
    search_fields = ['program_code', 'program_name', 'department']
    list_filter = ['sector', 'department']


@admin.register(Curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    list_display = ['program', 'year_level', 'semester']
    list_filter = ['year_level', 'semester', 'program']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['code', 'title', 'units', 'curriculum']
    search_fields = ['code', 'title']
    list_filter = ['curriculum__program', 'units']


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['section_name', 'subject', 'term', 'schedule', 'room', 'professor']
    list_filter = ['term', 'subject__curriculum__program']
    search_fields = ['subject__code', 'room']


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ['student', 'section', 'term', 'status', 'timestamp']
    list_filter = ['status', 'term']
    search_fields = ['student__student_number', 'section__subject__code']


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['applicant_name', 'email', 'program', 'status', 'timestamp']
    list_filter = ['status', 'program']
    search_fields = ['applicant_name', 'email']


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ['student', 'doc_type', 'uploaded_by', 'timestamp']
    list_filter = ['doc_type', 'timestamp']
    search_fields = ['student__student_number']