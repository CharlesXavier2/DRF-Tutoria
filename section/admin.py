from django.contrib import admin

# Register your models here.
from .models import Subject, ClassName, Chapter


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin) :
    list_display = ['id', 'name', 'slug']

@admin.register(ClassName)
class ClssNameAdmin(admin.ModelAdmin) :
    list_display = ['id', 'name', 'slug', 'get_subjects']

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin) :
    list_display = ['id', 'name', 'chapter_number', 'slug', 'classname', 'subject']
