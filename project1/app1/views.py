from rest_framework import viewsets
from.serializers import Student, StudentSerializer


class StudentviewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()


