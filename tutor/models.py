from django.db import models
from django.utils.text import slugify
from django.utils.timezone import now
from section.models import ClassName, Subject
# Create your models here.

DAYPART_CHOICES = (
    ('1', 'all'),
    ('2', 'morning'),
    ('3', 'evening'),
)

class Teachable(models.Model) :
    classname = models.ForeignKey(ClassName, related_name='+', on_delete=models.CASCADE)
    subjects = models.ManyToManyField(Subject)

    def get_subjects(self) :
        return ','.join([s.name for s in self.subjects.all()])
    
    def __str__(self):
        return self.classname.name + self.get_subjects()
    


class Tutor(models.Model) :
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=12, blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    teachables = models.ManyToManyField('Teachable', related_name='tutors', blank=True)
    daypart  = models.CharField(max_length=20, choices=DAYPART_CHOICES)
    timeslot_min = models.TimeField(default=now, auto_now_add=False)
    timeslot_max = models.TimeField(default=now, auto_now_add=False)

    

    # def save(self, *args, **kwargs) :
    #     if self.daypart == 'All' :
    #         self.timeslot_min = '01:00:00'
    #         self.timeslot_max = '23:00:00'
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.fname + ' ' + str(self.id)
    