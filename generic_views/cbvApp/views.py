from django.shortcuts import render

from cbvApp.models import Student
from cbvApp.serializers import StudentSerializer

from rest_framework import generics,mixins


# just call and use handler method

# non-primery key based operations
class StudentList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer
    
    def get(self,request):
        return self.list(request)
    
    def post(self,request):
        return self.create(request)


# primery key based operations

class StudentDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Student.objects.all()
    serializer_class= StudentSerializer

    def get(self,request,pk):
        return self.retrieve(request,pk)
    
    def put(self,request,pk):
        return self.update(request,pk)
    
    def delete(self,request,pk):
        return self.destroy(request,pk)




