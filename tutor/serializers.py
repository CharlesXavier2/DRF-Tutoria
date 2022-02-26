from rest_framework import serializers
from .models import Teachable, Tutor
from section.serializers import SubjectSlzr


class TeachableSlzr(serializers.ModelSerializer) :
    #subjects = SubjectSlzr(many=True)
    class Meta :
        model = Teachable
        fields = ['id', 'classname', 'subjects']
        read_only_fields = ['id']

class TutorSlzr(serializers.ModelSerializer) :
    #teachables = TeachableSlzr(many=True, required=False)
    # def create(self, validated_data):
    #     teachables = []
    #     id_teachables = validated_data.pop('teachables')
    #     tutor = Tutor.objects.create(**validated_data)
    #     for i in id_teachables:
    #         teachables.append(dict(Teachable.objects.get(pk=i)))
    #     tutor.teachables.add(**teachables)
    #     return tutor
    class Meta :
        model = Tutor
        fields = '__all__'
        read_only_fields = ['id']
        
        extra_kwargs = {'teachables': {'required': False, 'allow_null': True}}
    