# from rest_framework.serializers import Serializer
from rest_framework import serializers
from .models import Post, Comment
from django.conf import settings

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ['id', 'username', 'email']

class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'user' ]
    

class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Comment
        fields = ['id', 'post', 'content', 'user']