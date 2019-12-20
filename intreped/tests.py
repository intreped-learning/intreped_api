from rest_framework.test import APITestCase
from rest_framework import status
from .models import Teacher, Course, Badge, TeacherCourse, TeacherBadge
from .serializers import (TeacherReadSerializer, TeacherWriteSerializer,
                          CourseSerializer, TeacherCourseSerializer,
                          BadgeSerializer, TeacherBadgeSerializer)


class TeacherTestCase(APITestCase):

    def test_post_user(self):
        data = {"name": "Jason Bourne", "username": "TopAssassin",
                "password": "rememberEverything", "email": "jason@email.com"}
        response = self.client.post('/teachers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_all_users(self):
        response = self.client.get("/teachers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
