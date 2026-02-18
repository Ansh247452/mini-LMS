from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from accounts.views import CustomTokenObtainPairView
from .views import (
    index, register_view, courses_view,
    create_course_view, assignments_view,
    attendance_view, dashboard_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/', include('accounts.urls')),
    path('api/courses/', include('courses.urls')),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', index, name='index'),
    path('register/', register_view, name='register'),
    path('courses/', courses_view, name='courses'),
    path('create_course/', create_course_view, name='create_course'),
    path('assignments/<int:course_id>/', assignments_view, name='assignments'),
    path('attendance/<int:course_id>/', attendance_view, name='attendance'),
    path('dashboard/', dashboard_view, name='dashboard'),
]
