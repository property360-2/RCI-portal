# academics/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from .views import (
    # Authentication
    CustomTokenObtainPairView, register_view, logout_view,
    current_user_view, change_password_view,
    
    # ViewSets
    UserViewSet, ProgramViewSet, CurriculumViewSet, SubjectViewSet,
    SectionViewSet, StudentViewSet, EnrollmentViewSet, GradeViewSet,
    ApplicationViewSet, DocumentViewSet, AuditLogViewSet
)

# Create router for ViewSets
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'programs', ProgramViewSet, basename='program')
router.register(r'curriculums', CurriculumViewSet, basename='curriculum')
router.register(r'subjects', SubjectViewSet, basename='subject')
router.register(r'sections', SectionViewSet, basename='section')
router.register(r'students', StudentViewSet, basename='student')
router.register(r'enrollments', EnrollmentViewSet, basename='enrollment')
router.register(r'grades', GradeViewSet, basename='grade')
router.register(r'applications', ApplicationViewSet, basename='application')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'audit-logs', AuditLogViewSet, basename='auditlog')

urlpatterns = [
    # Authentication endpoints
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/register/', register_view, name='register'),
    path('auth/logout/', logout_view, name='logout'),
    path('auth/me/', current_user_view, name='current_user'),
    path('auth/change-password/', change_password_view, name='change_password'),
    
    # API routes (from router)
    path('', include(router.urls)),
]