from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('teachers', views.TeacherView)
router.register('courses', views.CourseView)
router.register('badges', views.BadgeView)
router.register('teacher_courses', views.TeacherCourseView)
router.register('teacher_badges', views.TeacherBadgeView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
