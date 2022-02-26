from rest_framework import serializers
from .models import Subject, Chapter, ClassName

class ClassNameSlzr(serializers.ModelSerializer) :
    class Meta :
        model = ClassName
        fields = '__all__'
        read_only_fields = ['id']

class SubjectSlzr(serializers.ModelSerializer) :
    chapters = serializers.StringRelatedField(many=True)
    class Meta:
        model = Subject
        fields = ['id', 'name', 'slug', 'chapters']
        read_only_fields = ['id']


class ChapterSlzr(serializers.ModelSerializer) :
    def validate(self, data) :
        classname = data.get('classname')
        subject = data.get('subject')
        chapter_number = data.get('chapter_number')
        ch = Chapter.objects.filter(classname=classname, subject=subject, chapter_number=chapter_number)
        if ch.exists() :
            raise serializers.ValidationError('Chapter Number {} Already Exists For Given Class And Subject'.format(chapter_number))
        else : 
            return data
    class Meta:
        model = Chapter
        fields = ['id', 'name', 'chapter_number', 'classname', 'subject']
        read_only_fields = ['id']