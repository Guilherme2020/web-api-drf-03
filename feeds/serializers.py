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


class CommentSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model: Comment
        fields = (
            'name',
           'email',
            'body',
            'post'

        )

