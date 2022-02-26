from rest_framework import serializers
from .models import Student, DemoClass, ClassRoom, ClassRoomReport




class StudentSlzr(serializers.ModelSerializer) :
    
    class Meta :
        model = Student
        fields = '__all__'
        read_only_fields = ['id']
        
class DemoClassSlzr(serializers.ModelSerializer) :
    
    class Meta :
        model = DemoClass
        fields = '__all__'
        read_only_fields = ['id']

class ClassRoomSlzr(serializers.ModelSerializer) :
    
    class Meta :
        model = ClassRoom
        fields = '__all__'
        read_only_fields = ['id']

class ClassRoomReportSlzr(serializers.ModelSerializer) :
    
    class Meta :
        model = ClassRoomReport
        fields = '__all__'
        read_only_fields = ['id']
        