from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Course, Lesson, Enrollment, Assignment, Submission, Attendance
from .serializers import (
    CourseSerializer, LessonSerializer, EnrollmentSerializer, 
    AssignmentSerializer, SubmissionSerializer, AttendanceSerializer
)

class IsInstructorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.role == 'INSTRUCTOR'

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsInstructorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(instructor=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[permissions.IsAuthenticated])
    def enroll(self, request, pk=None):
        course = self.get_object()
        if request.user.role == 'INSTRUCTOR':
             return Response({'detail': 'Instructors cannot enroll.'}, status=status.HTTP_400_BAD_REQUEST)
        
        Enrollment.objects.get_or_create(student=request.user, course=course)
        return Response({'status': 'enrolled'})

    @action(detail=True, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def students(self, request, pk=None):
        course = self.get_object()
        # Ensure user is instructor of this course
        if request.user != course.instructor:
            return Response({'detail': 'Not authorized.'}, status=status.HTTP_403_FORBIDDEN)
        
        enrollments = Enrollment.objects.filter(course=course)
        students = [e.student for e in enrollments]
        # We need a serializer for students. Let's use a simple list of dicts or import UserSerializer.
        # Simple for now:
        data = [{'id': s.id, 'username': s.username, 'email': s.email} for s in students]
        return Response(data)

    @action(detail=False, methods=['get'], permission_classes=[permissions.IsAuthenticated])
    def enrolled(self, request):
        if request.user.role == 'INSTRUCTOR':
             return Response([])
        enrollments = Enrollment.objects.filter(student=request.user)
        courses = [e.course for e in enrollments]
        serializer = self.get_serializer(courses, many=True)
        return Response(serializer.data)


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsInstructorOrReadOnly]

class AssignmentViewSet(viewsets.ModelViewSet):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsInstructorOrReadOnly]

class SubmissionViewSet(viewsets.ModelViewSet):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(student=self.request.user)

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        if user.role == 'INSTRUCTOR':
             return Attendance.objects.filter(course__instructor=user)
        return Attendance.objects.filter(student=user)
    
    def perform_create(self, serializer):
        # Ensure only instructor of the course can create attendance
        serializer.save() 
    
    @action(detail=False, methods=['post'])
    def mark_bulk(self, request):
        data = request.data
        course_id = data.get('course')
        date = data.get('date')
        records = data.get('records')

        if not all([course_id, date, records]):
            return Response({'detail': 'Missing data.'}, status=status.HTTP_400_BAD_REQUEST)

        # Verify instructor
        course = Course.objects.get(id=course_id)
        if request.user != course.instructor:
             return Response({'detail': 'Not authorized.'}, status=status.HTTP_403_FORBIDDEN)

        created_records = []
        for r in records:
            student_id = r.get('student')
            status_val = r.get('status')
            
            # Update or create
            obj, created = Attendance.objects.update_or_create(
                course=course,
                student_id=student_id,
                date=date,
                defaults={'status': status_val}
            )
            created_records.append(obj)
        
        return Response({'status': 'marked', 'count': len(created_records)}) 
