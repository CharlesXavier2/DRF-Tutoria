from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('student', views.StudentView, basename='student')
router.register('demo', views.DemoClassView, basename='demo')
router.register('classroom', views.ClassRoomView, basename='classroom')
router.register('report', views.ClassRoomReportView, basename='report')


urlpatterns = [
    
    path('', include(router.urls)),
    path('find-tutor/', views.find_tutor, name='find_tutor'),
    # path('demo-class/<str:user>/<int:pk>', views.demo_class, name='demo_class'),
    # path('demo-class/', views.demo_class, name='create_demo_class'),
    # path('class-room/<str:user>/<int:pk>', views.class_room, name='class_room'),
    # path('class-room/', views.class_room, name='create_class_room')
    
    
]