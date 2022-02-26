from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('tutor', views.GetTutors, basename='tutor')
router.register('teachable', views.GetTeachable, basename='teachable')

urlpatterns = [
    
    path('', include(router.urls)),
    
    
    
]