from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.reverse import reverse

#from feedit.feeds.serializers import
from .models import *
from rest_framework.response import Response


from .serializers import ProfileSerializer, PostSerializer, PostSerializerDetails,UserSerializer,CommentSerializer

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'profiles': reverse(ListProfileModel.name,request=request),
        })
class UserList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (
        permissions.IsAuthenticated,
    )
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (
        permissions.IsAuthenticated
    )

class ListProfileModel(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'list-profile'

class ListProfileModelDetail(generics.RetrieveAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'

class ListProfilePostsModel(generics.ListCreateAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'profile-post'

class ListProfilePostsModelDetail(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializerDetails
    name = 'profile-post-detail'
class ListPostCommentModel(generics.ListCreateAPIView):
    queryset =  Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'list-comment'