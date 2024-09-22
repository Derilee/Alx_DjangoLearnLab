from django.shortcuts import render
from django.conf import settings
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework import permissions


class PostPagination(PageNumberPagination):
    page_size = 10

class CommentPagination(LimitOffsetPagination):
    default_limit = 5

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    pagination_class = PostPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    authentication_classes = [TokenAuthentication]
    pagination_class = CommentPagination

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class FeedViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get_queryset(self):
        user = self.request.user
        following_users = user.following.all()
        return Post.objects.filter(user__in=following_users).order_by('-created_at')
    
#wrong code below
    # def get_queryset(self):
    #     author = self.request.user
    #     following_users = author.following.all()
    #     return Post.objects.filter(author__in=following_users).order_by('-created_at')