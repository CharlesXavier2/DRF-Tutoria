from rest_framework.generics import GenericAPIView
from rest_framework import viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from .models import Teachable, Tutor
from .serializers import TeachableSlzr, TutorSlzr

# Create your views here.

class GetTeachable(viewsets.ModelViewSet) :
    queryset = Teachable.objects.all()
    serializer_class = TeachableSlzr
class GetTutors(viewsets.ModelViewSet) :
    queryset = Tutor.objects.all()
    serializer_class = TutorSlzr

# @api_view(['GET','POST'])
# def get_tutors(request, pk=None) :
#     if request.method == "GET" :
#         res = {'msg':'Sample Response For Get Request'}
#         return Response(res) 
#     if request.method == "POST" :
#         res = {'msg':'Sample Response For POST Request'}
#         return Response(res) 