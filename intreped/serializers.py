from rest_framework import serializers
from .models import Course, Teacher, TeacherCourse


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ('id', 'title', 'description', 'url', 'thumbnail', 'category', 'duration')


class TeacherCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherCourse
        fields = ('id', 'teacher_id', 'course_id', 'current_time_marker',
                  'is_favorite', 'is_complete', 'is_in_progress')


class TeacherReadSerializer(serializers.ModelSerializer):
    teacher_courses = TeacherCourseSerializer(source='teachercourse_set', many=True)

    class Meta:
        model = Teacher
        fields = ('id', 'name', 'username', 'email', 'password', 'teacher_courses')


class TeacherWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'username', 'email', 'password', 'courses')
