from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CourseViewSet,
    LessonViewSet,
    AssignmentViewSet,
    SubmissionViewSet,
    AttendanceViewSet,
)



router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'lessons', LessonViewSet, basename='lesson')
router.register(r'assignments', AssignmentViewSet, basename='assignment')
router.register(r'submissions', SubmissionViewSet, basename='submission')
router.register(r'attendance', AttendanceViewSet, basename='attendance')

urlpatterns = [

    # ✅ ADD THIS ABOVE include(router.urls)
 

    path('', include(router.urls)),
]
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Course


@login_required
def my_courses_view(request):
    if request.user.role == "INSTRUCTOR":
        courses = Course.objects.filter(instructor=request.user)
    else:
        courses = Course.objects.all()   # change later to enrolled logic

    return render(request, "my_courses.html", {"courses": courses})
