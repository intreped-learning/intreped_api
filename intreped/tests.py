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


class CourseTestCase(APITestCase):

    def setUp(self):
        Course.objects.create(title='Learn This', description='This is important',
                              url='fakeurl.com', category='Important',
                              thumbnail='fakethumbnail.jpg', duration='4m25s')

    def test_create_a_course(self):
        data = {'title': 'Teach', 'description': 'How to teach',
                'url': 'randomurl.com', 'category': 'Teaching',
                'thumbnail': 'random.jpg', 'duration': '6m12s'}
        response = self.client.post('/courses/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Course.objects.count(), 2)
        self.assertEqual(response.data['title'], 'Teach')
        self.assertEqual(response.data['description'], 'How to teach')
        self.assertEqual(response.data['url'], 'randomurl.com')
        self.assertEqual(response.data['category'], 'Teaching')
        self.assertEqual(response.data['thumbnail'], 'random.jpg')
        self.assertEqual(response.data['duration'], '6m12s')

    def test_get_a_course(self):
        course_id = Course.objects.get(title='Learn This').id
        response = self.client.get(f'/courses/{course_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Learn This')
        self.assertEqual(response.data['description'], 'This is important')
        self.assertEqual(response.data['url'], 'fakeurl.com')
        self.assertEqual(response.data['category'], 'Important')
        self.assertEqual(response.data['thumbnail'], 'fakethumbnail.jpg')
        self.assertEqual(response.data['duration'], '4m25s')

    def test_get_all_courses(self):
        data = {'title': 'Teach', 'description': 'How to teach',
                'url': 'randomurl.com', 'category': 'Teaching',
                'thumbnail': 'random.jpg', 'duration': '6m12s'}
        self.client.post('/courses/', data)
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Learn This')
        self.assertEqual(response.data[0]['description'], 'This is important')
        self.assertEqual(response.data[0]['url'], 'fakeurl.com')
        self.assertEqual(response.data[0]['category'], 'Important')
        self.assertEqual(response.data[0]['thumbnail'], 'fakethumbnail.jpg')
        self.assertEqual(response.data[0]['duration'], '4m25s')

    def test_update_a_course(self):
        course_id = Course.objects.get(title='Learn This').id
        response = self.client.patch(f'/courses/{course_id}/', {'title': 'Do This NOW'})
        self.assertEqual(response.data['title'], 'Do This NOW')
        self.assertEqual(response.data['description'], 'This is important')
        self.assertEqual(response.data['url'], 'fakeurl.com')
        self.assertEqual(response.data['category'], 'Important')
        self.assertEqual(response.data['thumbnail'], 'fakethumbnail.jpg')
        self.assertEqual(response.data['duration'], '4m25s')

    def test_delete_a_course(self):
        course_id = Course.objects.get(title='Learn This').id
        response = self.client.delete(f'/courses/{course_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Course.objects.count(), 0)


class BadgeTestCase(APITestCase):

    def setUp(self):
        Badge.objects.create(category='Classroom Management')

    def test_create_a_badge(self):
        data = {'category': 'Engagement Strategies'}
        response = self.client.post('/badges/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Badge.objects.count(), 2)
        self.assertEqual(response.data['category'], 'Engagement Strategies')

    def test_get_a_badge(self):
        badge_id = Badge.objects.get(category='Classroom Management').id
        response = self.client.get(f'/badges/{badge_id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['category'], 'Classroom Management')

    def test_get_all_badges(self):
        data = {'category': 'Engagement Strategies'}
        self.client.post('/badges/', data)
        response = self.client.get('/badges/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['category'], 'Classroom Management')

    def test_update_a_badge(self):
        badge_id = Badge.objects.get(category='Classroom Management').id
        response = self.client.patch(f'/badges/{badge_id}/', {'category': 'Behavior Management'})
        self.assertEqual(response.data['category'], 'Behavior Management')

    def test_delete_a_badge(self):
        badge_id = Badge.objects.get(category='Classroom Management').id
        response = self.client.delete(f'/badges/{badge_id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Badge.objects.count(), 0)
