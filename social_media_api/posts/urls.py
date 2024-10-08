from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import PostViewSet, CommentViewSet, FeedViewSet, LikePostView, UnlikePostView
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'feed', FeedViewSet, basename='feed')

urlpatterns = [
    path('', include(router.urls)),
    path('api/posts-token-auth/', obtain_auth_token, name='posts-token-auth'),
    path('<int:pk>/like/', LikePostView.as_view(), name='like-post'),
    path('<int:pk>/unlike/', UnlikePostView.as_view(), name='unlike-post'),
    # path('feed/', FeedViewSet.as_view(), name='feed'),
]