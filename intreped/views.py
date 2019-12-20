from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets
from .models import Teacher
from .serializers import TeacherSerializer


class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
