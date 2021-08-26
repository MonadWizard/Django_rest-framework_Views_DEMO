from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer

from rest_framework import viewsets

# just call and use handler method
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


