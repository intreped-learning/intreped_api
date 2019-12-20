# from django.http import HttpResponse
# from django.shortcuts import render
from rest_framework import viewsets
from .mixins import ReadWriteSerializerMixin
from .models import Teacher, Course, TeacherCourse, Badge, TeacherBadge
from .serializers import (TeacherReadSerializer, TeacherWriteSerializer,
                          CourseSerializer, TeacherCourseSerializer,
                          BadgeSerializer, TeacherBadgeSerializer)


class CourseView(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class BadgeView(viewsets.ModelViewSet):
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer


class TeacherView(ReadWriteSerializerMixin, viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    read_serializer_class = TeacherReadSerializer
    write_serializer_class = TeacherWriteSerializer


class TeacherCourseView(viewsets.ModelViewSet):
    queryset = TeacherCourse.objects.all()
    serializer_class = TeacherCourseSerializer


class TeacherBadgeView(viewsets.ModelViewSet):
    queryset = TeacherBadge.objects.all()
    serializer_class = TeacherBadgeSerializer
