from django.contrib import admin

# Register your models here.
from .models import Student, DemoClass, ClassRoom, ClassRoomReport


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin) :
    list_display = ['id', 'fname']

@admin.register(DemoClass)
class DemoClassAdmin(admin.ModelAdmin) :
    list_display = ['student', 'tutor', 'scheduled_at']

@admin.register(ClassRoom)
class ClassRoomAdmin(admin.ModelAdmin) :
    list_display = ['student', 'tutor']

@admin.register(ClassRoomReport)
class ClassRoomReportAdmin(admin.ModelAdmin) :
    list_display = ['classroom', 'created_at']