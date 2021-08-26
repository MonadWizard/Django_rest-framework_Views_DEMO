from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('std',views.StudentViewSet)
router.register('rostd',views.StudentReadOnlyViewSet)

urlpatterns = [
    path('', include(router.urls)),

]