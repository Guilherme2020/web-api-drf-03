from django.shortcuts import render

# Create your views here.
from rest_framework import mixins
from rest_framework.generics import GenericAPIView
from .models import *
from rest_framework.response import Response

#from feedit.feeds.models import Profile

from .serializers import ProfileSerializer


class ListProfileModel(mixins.ListModelMixin):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self,request):
        query_set = self.get_queryset()
        serializer = ProfileSerializer(query_set, many=True)
        return Response(serializer.data)

class RetrieveModel(mixins.RetrieveModelMixin):
    pass

#class ListCreateAPIView(mixins.ListModelMixin,mixins.CreateModelMixin,GenericAPIView):
    #queryset =
    ##serializer_class =
    #name = ''