from django.shortcuts import render
from django.http import JsonResponse
from firstApp.models import Employee

# Create your views here.
def employeeView(request):
    emp = {
    'id':123,
    'name':'John',
    'sal':100000000
    }

    data = Employee.objects.all();
    response = {'employees':list(data.values('name','sal'))}

    return JsonResponse(response)
