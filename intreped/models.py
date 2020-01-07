from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=1000)
    url = models.CharField(max_length=300, unique=True)
    category = models.CharField(max_length=50)
    thumbnail = models.CharField(max_length=300, unique=True)
    duration = models.CharField(max_length=20)


class Badge(models.Model):
    category = models.CharField(max_length=50, unique=True)


class Teacher(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, unique=True)
    password = models.CharField(max_length=20)
    email = models.CharField(max_length=50, unique=True)
    courses = models.ManyToManyField(Course, through='TeacherCourse')
    badges = models.ManyToManyField(Badge, through='TeacherBadge')


class TeacherCourse(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    current_time_marker = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)
    is_complete = models.BooleanField(default=False)
    is_in_progress = models.BooleanField(default=False)

    class Meta:
        unique_together = ('teacher_id', 'course_id',)


class TeacherBadge(models.Model):
    teacher_id = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    badge_id = models.ForeignKey(Badge, on_delete=models.CASCADE)
    cumulative_time = models.CharField(max_length=10)

    class Meta:
        unique_together = ('teacher_id', 'badge_id',)
