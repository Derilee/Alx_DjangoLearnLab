from django.urls import path, include
# from .views import BookList,
from. views import BookViewSet
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


router = DefaultRouter()
# router.register(r'BookList', BookViewSet)
router.register(r'books', BookViewSet, basename='book')


urlpatterns = [
    # path('api/books/', BookList.as_view(), name='book-list'),
    path('api/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]

