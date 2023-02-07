from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from app1.views import StudentviewSet

router = DefaultRouter()

router.register('student', StudentviewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
