from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('subject', views.SubjectView, basename='subject')
router.register('class', views.ClassNameView, basename='classname')
router.register('chapter', views.ChapterView, basename='chapter')


urlpatterns = [
    path('', include(router.urls))
    # path('classes/', views.get_classes, name='classes'),
    # path('classes/<int:pk>', views.get_classes, name='classes'),
    # path('allsubjects/', views.get_subjects, name='all_subjects'),
    # path('allsubjects/<int:pk>', views.get_subjects, name='all_subjects'),
    # path('addsubject/', views.add_subject, name='add_subject'),
    # path('chapter/', views.chapter, name='all_chapters'),
    # path('chapter/<int:pk>', views.chapter, name='chapter'),
    


    
]