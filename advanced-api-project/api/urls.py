from django.urls import path, include
from .views import BookCreateView, BookListView, BookDetailView, BookDeleteView, BookUpdateView, AuthorListView, AuthorDetailView
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('authors', AuthorListView.as_view(), name='author-list'),
    path('authors/<int:pk>', AuthorDetailView.as_view(),name='author-detail'),
    path('books', BookListView.as_view(), name='book-list'),
    path('books/create', BookCreateView.as_view(), name='create-books'),
    path('books/<int:pk>', BookDetailView.as_view(), name='books-details'),
    path('books/delete/<int:pk>', BookDeleteView.as_view(), name='delete-books'),
    path('books/update/<int:pk>', BookUpdateView.as_view(), name='update-books'),
    path('api-token-auth/', obtain_auth_token, name='auth-token-auth'),
]