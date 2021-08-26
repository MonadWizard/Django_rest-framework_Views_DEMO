from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer

from rest_framework import generics


# just call and use handler method

# non-primery key based operations
class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer


# primery key based operations
class StudentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer


