from rest_framework.test import APITestCase
from rest_framework import status
from .models import Teacher, Course, Badge, TeacherCourse, TeacherBadge
from .serializers import (TeacherReadSerializer, TeacherWriteSerializer,
                          CourseSerializer, TeacherCourseSerializer,
                          BadgeSerializer, TeacherBadgeSerializer)


class TeacherTestCase(APITestCase):

    def setUp(self):
        Teacher.objects.create(name='Mr. Apple', username='apple123',
                               password='password', email='apple@email.com')

    def test_create_a_teacher(self):
        data = {'name': 'Jason Bourne', 'username': 'TopAssassin',
                'password': 'rememberEverything', 'email': 'jason@email.com'}
        response = self.client.post('/teachers/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Teacher.objects.count(), 2)
        self.assertEqual(response.data['name'], 'Jason Bourne')
        self.assertEqual(response.data['username'], 'TopAssassin')
        self.assertEqual(response.data['password'], 'rememberEverything')
        self.assertEqual(response.data['email'], 'jason@email.com')

    def test_get_a_teacher(self):
        teacher_id = Teacher.objects.get(name='Mr. Apple').id
        response = self.client.get(f'/teachers/{teacher_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Mr. Apple')
        self.assertEqual(response.data['username'], 'apple123')
        self.assertEqual(response.data['password'], 'password')
        self.assertEqual(response.data['email'], 'apple@email.com')
        self.assertEqual(response.data['teacher_courses'], [])
        self.assertEqual(response.data['teacher_badges'], [])

    def test_get_all_teachers(self):
        data = {'name': 'Jason Bourne', 'username': 'TopAssassin',
                'password': 'rememberEverything', 'email': 'jason@email.com'}
        self.client.post('/teachers/', data)
        response = self.client.get('/teachers/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['name'], 'Mr. Apple')
        self.assertEqual(response.data[0]['username'], 'apple123')
        self.assertEqual(response.data[0]['password'], 'password')
        self.assertEqual(response.data[0]['email'], 'apple@email.com')
        self.assertEqual(response.data[0]['teacher_courses'], [])
        self.assertEqual(response.data[0]['teacher_badges'], [])

    def test_update_a_teacher(self):
        teacher_id = Teacher.objects.get(name='Mr. Apple').id
        response = self.client.patch(f'/teachers/{teacher_id}/', {'name': 'Frank Apple'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Frank Apple')
        self.assertEqual(response.data['username'], 'apple123')
        self.assertEqual(response.data['password'], 'password')
        self.assertEqual(response.data['email'], 'apple@email.com')

    def test_delete_a_teacher(self):
        teacher_id = Teacher.objects.get(name='Mr. Apple').id
        response = self.client.delete(f'/teachers/{teacher_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Teacher.objects.count(), 0)
