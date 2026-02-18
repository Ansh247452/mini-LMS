from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def register_view(request):
    return render(request, 'register.html')

def courses_view(request):
    return render(request, 'courses.html')

def create_course_view(request):
    return render(request, 'create_course.html')

def assignments_view(request, course_id):
    return render(request, 'assignments.html', {'course_id': course_id})

def attendance_view(request, course_id):
    return render(request, 'attendance.html', {'course_id': course_id})

def dashboard_view(request):
    return render(request, 'dashboard.html')
