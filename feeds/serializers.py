from rest_framework import serializers

from .models import *


class  PostSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Post
        fields = (
            'title','body','user'
        )

class ProfileSerializer(serializers.HyperlinkedModelSerializer):
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
