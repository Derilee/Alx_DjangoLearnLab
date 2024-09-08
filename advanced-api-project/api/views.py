from django.shortcuts import render
from .models import Book, Author
from rest_framework import generics, serializers, filters
from .seriealizers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import PermissionDenied
from django_filters.rest_framework import DjangoFilterBackend


# AuthorListView: Handles retrieving all authors and creating new authors.
# Anyone can view the authors (read-only access), but only authenticated users can add new authors.
class AuthorListView(generics.ListCreateAPIView):
    queryset = Author.objects.all()  # Fetches all authors from the database
    serializer_class = AuthorSerializer  # Uses AuthorSerializer to display the data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users can add, but anyone can view


# AuthorDetailView: Handles retrieving, updating, or deleting a specific author by their ID.
# Anyone can view the details of an author, but only authenticated users can update or delete them.
class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()  # Fetches all authors
    serializer_class = AuthorSerializer  # Uses AuthorSerializer for displaying and updating
    permission_classes = [IsAuthenticatedOrReadOnly]  # Authenticated users can edit, others can only view


# BookListView: Handles retrieving all books in the database.
# Anyone can view the list of books.
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Uses BookSerializer to display book data
    permission_classes = [IsAuthenticatedOrReadOnly]  # Read-only access for unauthenticated users
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

    # def get_queryset(self):
    #     queryset = Book.objects.all()
    #     author_id = self.request.query_params.get('author')
    #     if author_id:
    #         queryset = queryset.filter(author__id=author_id)
    #     return queryset


# BookDetailView: Handles retrieving details of a specific book by its ID.
# Anyone can view the details of a book.
class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()  # Fetches a specific book by its ID
    serializer_class = BookSerializer  # Uses BookSerializer to display the details of the book
    permission_classes = [IsAuthenticatedOrReadOnly]  # Only view access, no edit without authentication


# BookCreateView: Allows authenticated users to create new books.
# Only authenticated users can add new books to the system.
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()  # Fetches all books
    serializer_class = BookSerializer  # Uses BookSerializer for creating new books
    authentication_classes = [TokenAuthentication]  # Requires token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can create books

    # Override the method to add custom behavior when creating a book
    def perform_create(self, serializer):
        # Check if the user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Only authenticated users can create books")
        serializer.save()  # Save the new book if authentication passes


# BookUpdateView: Allows authenticated users to update book details.
# The user must be authenticated to edit the book.
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()  # Fetches the book to be updated
    serializer_class = BookSerializer  # Uses BookSerializer to update the book
    lookup_field = 'pk'  # Looks up the book by its primary key (ID)
    authentication_classes = [TokenAuthentication]  # Requires token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can update books

    # Override the method to add custom behavior when updating a book
    def perform_update(self, serializer):
        # Check if the user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Only authenticated users can update books")
        serializer.save()  # Save the updated book if authentication passes


# BookDeleteView: Allows authenticated users to delete books.
# Only authenticated users can delete a book.
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()  # Fetches the book to be deleted
    serializer_class = BookSerializer  # Uses BookSerializer to display the book being deleted
    lookup_field = 'pk'  # Looks up the book by its primary key (ID)
    authentication_classes = [TokenAuthentication]  # Requires token-based authentication
    permission_classes = [IsAuthenticated]  # Only authenticated users can delete books

    # Override the method to add custom behavior when deleting a book
    def perform_destroy(self, instance):
        # Check if the user is authenticated
        if not self.request.user.is_authenticated:
            raise PermissionDenied("Only authenticated users can delete books")
        super().perform_destroy(instance)  # Perform the deletion if authentication passes
