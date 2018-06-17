from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.generics import GenericAPIView
from rest_framework.reverse import reverse
from rest_framework.throttling import ScopedRateThrottle
from rest_framework.authtoken.models import Token

#from feedit.feeds.serializers import
from .models import *
from rest_framework.response import Response

from .permissions import IsOwnerPost, IsOwnerPostFromCommentRelated

from .serializers import ProfileSerializer, PostSerializer, PostSerializerDetails,UserSerializer,CommentSerializer
from rest_framework.authtoken.views import obtain_auth_token

class CustomAuthToken(ObtainAuthToken):

    throttle_scope = 'api-token'
    throttle_classes = (ScopedRateThrottle, )


    def post(self,request,*args,**kwargs):

        serializer  = self.serializer_class(data=request.data,
                                            context={
                                                'request': request
                                            })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id': user.pk,
            'name': user.name,

        })

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self,request,*args,**kwargs):
        return Response({
            'profiles': reverse(ListProfileModel.name,request=request),
            'comments': reverse(ListPostCommentModel.name,request=request),
            'users':reverse(UserList.name,request=request)
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

class ListProfileModel(generics.ListCreateAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'list-profile'
    permission_classes = (
        permissions.IsAuthenticated,
    )

class ListProfileModelDetail(generics.RetrieveAPIView):

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    name = 'profile-detail'
    permission_classes = (
        permissions.IsAuthenticated,
    )

class ListProfilePostsModel(generics.ListCreateAPIView,):

    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'profile-post'
    permission_classes = (
        IsOwnerPost,
        permissions.IsAuthenticated,
    )

class ListProfilePostsModelDetail(generics.RetrieveAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    name = 'profile-post-detail'
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerPost
    )

class ListPostCommentModel(generics.ListCreateAPIView,):
    queryset =  Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'list-comment'
    permission_classes = (
        IsOwnerPost,
        permissions.IsAuthenticated,
    )
class ListPostCommentModelDetail(generics.RetrieveAPIView,generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    name = 'list-comment-detail'
    permission_classes = (
        permissions.IsAuthenticated,
        IsOwnerPostFromCommentRelated
    )