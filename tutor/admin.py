from django.contrib import admin

# Register your models here.
from .models import Teachable, Tutor

@admin.register(Teachable)
class TeachableAdmin(admin.ModelAdmin) :
    list_display = ['classname', 'get_subjects']

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin) :
    list_display = ['fname']