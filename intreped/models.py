from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    category = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=300)
    duration = models.CharField(max_length=20)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    courses = models.ManyToManyField(Course, through='TeacherCourse')


class TeacherCourse(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    current_time_marker = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    is_in_progress = models.BooleanField(default=False)
