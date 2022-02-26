from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import SubjectSlzr, ChapterSlzr, ClassNameSlzr
from .models import Subject, Chapter, ClassName

class SubjectView(viewsets.ModelViewSet) :
    queryset = Subject.objects.all()
    serializer_class = SubjectSlzr

class ClassNameView(viewsets.ModelViewSet) :
    queryset = ClassName.objects.all()
    serializer_class = ClassNameSlzr


class ChapterView(viewsets.ModelViewSet) :
    queryset = Chapter.objects.all()
    serializer_class = ChapterSlzr
    filterset_fields = ['classname', 'subject']


# @api_view(['GET', 'POST', 'PUT'])
# def chapter(request, pk=None) :
#     if request.method == "GET" :
#         id = pk
#         if id is not None :
#             chapter = get_object_or_404(Chapter, pk=id)
#             slzr = ChapterSlzr(chapter) 
#             return Response(slzr.data, status=status.HTTP_200_OK)
#         else :
#             chapter = Chapter.objects.all()
#             slzr = ChapterSlzr(chapter, many=True)
#             return Response(slzr.data, status=status.HTTP_200_OK)
#     if request.method == "POST" :
#         slzr = ChapterSlzr(data=request.data)
#         if slzr.is_valid() :
#             slzr.save()
#             res = {'msg' : 'Chapter Created Successfully'}
#             return Response(res, status=status.HTTP_200_OK) 
#         else : 
#             return Response(slzr.errors, status=status.HTTP_400_BAD_REQUEST) 
        
        
