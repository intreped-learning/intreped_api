from django.db import models


class Teacher(models.Model):
    name = models.CharField(max_length=60)
