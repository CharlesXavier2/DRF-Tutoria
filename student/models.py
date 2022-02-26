from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
from section.models import ClassName, Subject, Chapter
from tutor.models import Tutor, Teachable, DAYPART_CHOICES


class Student(models.Model) :
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    aadhar = models.CharField(max_length=12, blank=True, null=True)
    classname = models.ForeignKey(ClassName, related_name='students', on_delete=models.CASCADE)

    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    
    daypart  = models.CharField(max_length=20, choices=DAYPART_CHOICES)
    timeslot_min = models.TimeField(default=now, auto_now_add=False)
    timeslot_max = models.TimeField(default=now, auto_now_add=False)

    

    
    def __str__(self):
        return self.fname + ' ' + str(self.id)

class DemoClass(models.Model) :
    student = models.ForeignKey(Student, related_name='democlasses', on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, related_name='democlasses', on_delete=models.CASCADE)
    teachables = models.ManyToManyField(Teachable)
    created_at = models.DateField(auto_now_add=True)
    scheduled_at = models.DateTimeField()
    is_active = models.BooleanField(default=True)   

class ClassRoom(models.Model) :
    student = models.ForeignKey(Student, related_name='classrooms', on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, related_name='classrooms', on_delete=models.CASCADE)
    teachables = models.ManyToManyField(Teachable)
    created_at = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class ClassRoomReport(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    report_date = models.DateField(default=now, auto_now_add=False)
    # refernce to others 
    classroom = models.ForeignKey(ClassRoom, related_name='report', on_delete=models.CASCADE)
    classname = models.ForeignKey(ClassName, related_name='+', on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, related_name='+', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='+', on_delete=models.CASCADE)

    # entry status
    homework_percentage = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(1)])
    percentage_finished = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(1)])

    #boolean flags..
    is_notes_done = models.BooleanField(default=False)
    is_qna_done = models.BooleanField(default=False)
    is_memorized = models.BooleanField(default=False)
    is_test_done = models.BooleanField(default=False)

    

    class Meta:
        ordering = ('-created_at',)