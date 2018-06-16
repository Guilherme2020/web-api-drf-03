from rest_framework import serializers

from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = (
            'username','email',
        )
class AddressSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Address
        fields = ('zipcode','street','city','suite')
class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    address = AddressSerializer()
    user =  UserSerializer()
    class Meta:
        model = Profile
        fields = (
            'user','address'
        )
class  PostSerializer(serializers.HyperlinkedModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Post
        fields = (
            'title','body','profile'
        )

class PostSerializerDetails(serializers.HyperlinkedModelSerializer):

   # post = PostSerializer()
   # profile = ProfileSerializer()
    #count_comments =  serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('url','title')

    def get_count_comments(self,obj):
        post = Post.objects.get(id=obj.pk)
        quantidade = Comment.objects.filter(post=post).count()
        return quantidade
class CommentSerializer(serializers.HyperlinkedModelSerializer):
    post = PostSerializer()
    class Meta:
        model = Comment
        fields = (
            'name',
            'email',
            'body',
            'post'

        )

#CommentSerializerDetails(serializers.)