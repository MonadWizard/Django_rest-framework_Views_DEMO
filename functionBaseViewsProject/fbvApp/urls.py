from django.urls import path
from .import views

urlpatterns = [
    path('s/', views.student_list),
    path('s/<int:pk>', views.student_detail),
]
