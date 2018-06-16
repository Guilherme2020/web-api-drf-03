from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, permissions
from rest_framework.generics import GenericAPIView
from rest_framework.reverse import reverse

#from feedit.feeds.serializers import
from .models import *
from rest_framework.response import Response

from .permissions import IsOwnerPost, IsOwnerPostFromCommentRelated

from .serializers import ProfileSerializer, PostSerializer, PostSerializerDetails,UserSerializer,CommentSerializer

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'profiles': reverse(ListProfileModel.name,request=request),
            'comments': reverse(ListPostCommentModel.name,request=request)
        })

    #permission_classes = (
    #    permissions.IsAuthenticated,
    #)
class UserList(generics.ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-list'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly,
    )
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    name = 'user-detail'
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly
    )

class ListProfileModel(generics.ListCreateAPIView,generics.DestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'list-profile'
    permission_classes = (
        permissions.IsAuthenticated,
    )

class ListProfileModelDetail(generics.RetrieveAPIView,generics.DestroyAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )

class ListProfilePostsModel(generics.ListCreateAPIView,generics.DestroyAPIView):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'profile-post'
    permission_classes = (
        IsOwnerPost,
        permissions.IsAuthenticated,
    )

class ListProfilePostsModelDetail(generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'profile-post-detail'
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerPost
    )

class ListPostCommentModel(generics.ListCreateAPIView,generics.DestroyAPIView):
    queryset =  Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'list-comment'
    permission_classes = (
        IsOwnerPost,
        permissions.IsAuthenticated,
    )
class ListPostCommentModelDetail(generics.RetrieveAPIView,generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'list-comment-detail'
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerPostFromCommentRelated
    )