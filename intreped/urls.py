from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teachers', views.TeacherView)
router.register('courses', views.CourseView)
router.register('teacher_courses', views.TeacherCourseView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
