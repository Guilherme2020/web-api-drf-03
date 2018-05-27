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

class  PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = (
            'title','body','user'
        )

class ProfileSerializer(serializers.HyperlinkedModelSerializer):

    address = AddressSerializer()
    user =  UserSerializer()
    class Meta:
        model = Profile
        fields = (
            'user','address'
        )
class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model: Comment
        fields = (
            'name',
           'email',
            'body',
            'post'

        )

