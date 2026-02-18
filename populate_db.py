import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from django.contrib.auth import get_user_model
from courses.models import Course, Lesson, Assignment, Enrollment

User = get_user_model()

def populate():
    # Create Instructor
    instructor, created = User.objects.get_or_create(
        username='instructor',
        defaults={'email': 'instructor@example.com', 'role': 'INSTRUCTOR'}
    )
    if created:
        instructor.set_password('pass1234')
        instructor.save()
        print("Created Instructor: instructor / pass1234")
    else:
        print("Instructor already exists")

    # Create Student
    student, created = User.objects.get_or_create(
        username='student',
        defaults={'email': 'student@example.com', 'role': 'STUDENT'}
    )
    if created:
        student.set_password('pass1234')
        student.save()
        print("Created Student: student / pass1234")
    else:
        print("Student already exists")

    # Create Course
    course, created = Course.objects.get_or_create(
        title='Intro to Django',
        defaults={
            'description': 'Learn the basics of Django and DRF.',
            'instructor': instructor
        }
    )
    if created:
        print(f"Created Course: {course.title}")
    else:
        print(f"Course already exists: {course.title}")

    # Create Lesson
    lesson, created = Lesson.objects.get_or_create(
        course=course,
        title='Setting up Django',
        defaults={
            'content': 'First, install django using pip install django...',
            'order': 1
        }
    )
    if created:
        print(f"Created Lesson: {lesson.title}")

    # Create Assignment
    assignment, created = Assignment.objects.get_or_create(
        course=course,
        title='Create a Project',
        defaults={
            'description': 'Initialize a new Django project and run the server.',
            'due_date': '2026-12-31 23:59:59'
        }
    )
    if created:
        print(f"Created Assignment: {assignment.title}")

    # Enroll Student
    enrollment, created = Enrollment.objects.get_or_create(
        student=student,
        course=course
    )
    if created:
        print("Enrolled student in course")

if __name__ == '__main__':
    populate()
