from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics
from rest_framework.generics import GenericAPIView
from .models import *
from rest_framework.response import Response

#from feedit.feeds.models import Profile

from .serializers import ProfileSerializer


class ListProfileModel(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'list-profile'

    # def list(self,request):
    #     query_set = self.get_queryset()
    #     serializer = ProfileSerializer(query_set, many=True)
    #     return Response(serializer.data)

class ListProfileModelDetail(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

#class ListCreateAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    #queryset =
    ##serializer_class =
    #name = ''