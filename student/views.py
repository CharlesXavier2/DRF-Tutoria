from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from .models import Student, DemoClass, ClassRoom, ClassRoomReport
from section.models import ClassName, Subject
from tutor.models import Teachable, Tutor
from .serializers import StudentSlzr, DemoClassSlzr, ClassRoomSlzr, ClassRoomReportSlzr
from tutor.serializers import TutorSlzr
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

class StudentView(viewsets.ModelViewSet) :
    queryset = Student.objects.all()
    serializer_class = StudentSlzr

class DemoClassView(viewsets.ModelViewSet) :
    queryset = DemoClass.objects.all()
    serializer_class = DemoClassSlzr
    filterset_fields = ['tutor', 'student']

class ClassRoomView(viewsets.ModelViewSet) :
    queryset = ClassRoom.objects.all()
    serializer_class = ClassRoomSlzr
    filterset_fields = ['tutor', 'student']

class ClassRoomReportView(viewsets.ModelViewSet) :
    queryset = ClassRoomReport.objects.all()
    serializer_class = ClassRoomReportSlzr
    filterset_fields = ['report_date', 'classroom']

@api_view(['POST'])
def find_tutor(request) :
    if request.method == "POST" :
        tutor_list = []
        data = request.data
        c = data['classname']
        cname = get_object_or_404(ClassName, pk=c)
        subs  = data['subjects']
        if not cname or not subs : return Response({"msg": 'Bad Request'})
        subject_list = []
        for sub in subs :
            subject = get_object_or_404(Subject, pk=int(sub))
            subject_list.append(subject)
        tutors = Tutor.objects.all()
        for tutor in tutors :
            for tbl in tutor.teachables.all() :
                # print(tbl.classname)
                # print(tbl.subjects.all())
                if tbl.classname == cname and set(subject_list).issubset(set(tbl.subjects.all())) :
                    print(tutor_list)
                    tutor_list.append(tutor)
        slzr = TutorSlzr(tutor_list, many=True)
        if slzr.data : 
            return Response(slzr.data)           
        res = {"msg": 'Bad Request'}
        return Response(res)

# @api_view(['GET', 'POST'])
# def demo_class(request, pk=None, user=None) :
#     if request.method == "GET" :
#         data = request.data
#         if pk is None and user is None : 
#             demo = DemoClass.objects.all()
#             slzr = DemoClassSlzr(demo, many=True)
#             return Response(slzr.data)
#         if user == 'tutor' :
#             demo = DemoClass.objects.filter(tutor_id=pk)
#             slzr = DemoClassSlzr(demo, many=True)
#             return Response(slzr.data)
#         elif user == 'student' :
#             demo = DemoClass.objects.filter(student_id=pk)
#             slzr = DemoClassSlzr(demo, many=True)
#             return Response(slzr.data)
#         return Response({'msg' : 'Bad Request'})

#     if request.method == "POST" :
#         data = request.data
#         slzr = DemoClassSlzr(data=data)
#         if slzr.is_valid() :
#             slzr.save()
#             return Response(slzr.data)
#         else : 
#             return Response({'msg' : 'Bad Request'})

# @api_view(['GET', 'POST'])
# def class_room(request, pk=None, user=None) :
#     if request.method == "GET" :
#         data = request.data
#         if pk is None and user is None : 
#             croom = ClassRoom.objects.all()
#             slzr = ClassRoomSlzr(croom, many=True)
#             return Response(slzr.data)
#         if user == 'tutor' :
#             croom = ClassRoom.objects.filter(tutor_id=pk)
#             slzr = ClassRoomSlzr(croom, many=True)
#             return Response(slzr.data)
#         elif user == 'student' :
#             croom = ClassRoom.objects.filter(student_id=pk)
#             slzr = ClassRoomSlzr(croom, many=True)
#             return Response(slzr.data)
#         return Response({'msg' : 'Bad Request'})

#     if request.method == "POST" :
#         data = request.data
#         slzr = ClassRoomSlzr(data=data)
#         if slzr.is_valid() :
#             slzr.save()
#             return Response(slzr.data)
#         else : 
#             return Response({'msg' : 'Bad Request'})



            