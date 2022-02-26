from django.db import models
from django.utils.text import slugify
# Create your models here.

class Subject(models.Model) :
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True, unique=True)

    def save(self, *args, **kwargs ) :
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
    

class ClassName(models.Model) :
    name = models.CharField(max_length=50)
    slug = models.SlugField(default='', blank=True, unique=True)
    subjects = models.ManyToManyField(Subject)

    def save(self, *args, **kwargs ) :
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.slug
    
    def get_subjects(self) :
        return ','.join([s.name for s in self.subjects.all()])


class Chapter(models.Model) :
    name = models.CharField(max_length=100, null=False, blank=False)
    chapter_number = models.PositiveIntegerField(null=False, default=1)
    classname = models.ForeignKey(ClassName, related_name='+', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='chapters', on_delete=models.CASCADE)
    
    slug = models.CharField(max_length=100, null=False, blank=True)
    
    def __str__(self):
        return str(self.chapter_number) + ':' + self.slug + '-' + self.subject.slug + '-' + self.classname.slug
    
    def save(self, *args, **kwargs ) :
        self.slug = slugify(self.name, allow_unicode=True)
        super().save(*args, **kwargs)