# academics/permissions.py

from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allow access only to users with 'admin' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admin'


class IsRegistrar(permissions.BasePermission):
    """
    Allow access only to users with 'registrar' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'registrar'


class IsAdmission(permissions.BasePermission):
    """
    Allow access only to users with 'admission' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'admission'


class IsHead(permissions.BasePermission):
    """
    Allow access only to users with 'head' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'head'


class IsProfessor(permissions.BasePermission):
    """
    Allow access only to users with 'professor' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'professor'


class IsStudent(permissions.BasePermission):
    """
    Allow access only to users with 'student' role.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.role == 'student'


class IsAdminOrRegistrar(permissions.BasePermission):
    """
    Allow access to admins or registrars.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'registrar'])


class IsAdminOrHead(permissions.BasePermission):
    """
    Allow access to admins or department heads.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'head'])


class IsStaffUser(permissions.BasePermission):
    """
    Allow access to all staff (admin, registrar, admission, head).
    Students and professors are excluded.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'registrar', 'admission', 'head'])


class IsOwnerOrStaff(permissions.BasePermission):
    """
    Allow owners to access their own data, or staff to access any data.
    Used for student profiles, enrollments, grades, etc.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        # Staff can access any object
        if request.user.role in ['admin', 'registrar', 'head']:
            return True
        
        # Students can only access their own data
        if request.user.role == 'student':
            # Check if object has a student field
            if hasattr(obj, 'student'):
                return obj.student.user == request.user
            # Check if object has a user field
            if hasattr(obj, 'user'):
                return obj.user == request.user
        
        # Professors can access data for their sections
        if request.user.role == 'professor':
            if hasattr(obj, 'section'):
                return obj.section.professor == request.user
        
        return False


class CanManageGrades(permissions.BasePermission):
    """
    Professors can manage grades for their sections.
    Registrars and admins can manage all grades.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'registrar', 'professor'])
    
    def has_object_permission(self, request, view, obj):
        # Admin and registrar can modify any grade
        if request.user.role in ['admin', 'registrar']:
            return True
        
        # Professors can only modify grades for their sections
        if request.user.role == 'professor':
            return obj.section.professor == request.user
        
        return False


class CanEnroll(permissions.BasePermission):
    """
    Students can enroll themselves.
    Registrars and admins can enroll any student.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'registrar', 'student'])


class ReadOnlyOrStaff(permissions.BasePermission):
    """
    Read-only access for everyone.
    Write access only for staff (admin, registrar, head).
    """
    def has_permission(self, request, view):
        # Allow read operations for authenticated users
        if request.method in permissions.SAFE_METHODS:
            return request.user and request.user.is_authenticated
        
        # Write operations only for staff
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'registrar', 'head'])


class CanManageCurriculum(permissions.BasePermission):
    """
    Only admins and heads can manage curriculum.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'head'])


class CanManageApplications(permissions.BasePermission):
    """
    Only admission officers and admins can manage applications.
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'admission'])


class CanViewAnalytics(permissions.BasePermission):
    """
    Different roles have different analytics access:
    - Admin: All analytics
    - Head: Department analytics
    - Registrar: Limited analytics
    - Professor: Class analytics
    """
    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated and 
                request.user.role in ['admin', 'head', 'registrar', 'professor'])


# ========================================
# HELPER FUNCTION FOR ROLE CHECKING
# ========================================

def has_role(user, roles):
    """
    Helper function to check if user has one of the specified roles.
    
    Usage:
        if has_role(request.user, ['admin', 'registrar']):
            # Do something
    """
    if not user or not user.is_authenticated:
        return False
    
    if isinstance(roles, str):
        roles = [roles]
    
    return user.role in roles