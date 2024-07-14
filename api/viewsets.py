from rest_framework import viewsets
from api.models import Student, Semester, Program, Enrollment, Lecturer
from api.serializers import StudentSerializer, SemesterSerializer, ProgramSerializer, EnrollmentSerializer, \
    LecturerSerializer


class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class SemesterViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Semester.objects.all()
    serializer_class = SemesterSerializer

class ProgramViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

class LecturerViewSet(viewsets.ModelViewSet):
    queryset = Lecturer.objects.all()
    serializer_class = LecturerSerializer

class EnrollmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer