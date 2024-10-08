# query all books by a specific author
from relationship_app.models import Book, Author
author_name = "some author name"
author = Author.objects.get(name=author_name)
book_author = Book.objects.filter(author=author)
for book in book_author:
    print(book.title)



# List all books in a library
from relationship_app.models import Library
library_name = "Some Library Name"
all_libraries = Library.objects.get(name=library_name)
all_books = all_libraries.books.all()
print(f"library name: {all_libraries.name}")
for book in all_books:
        print(f"book:{book.title}")


# retrieve a librarian from a library
from relationship_app.models import Librarian
library = Library.objects.get(name= "Library name")
librarian = Librarian.objects.get(library=library)
print(f"librarian{librarian.name}")
print(f"library{librarian.library.name}")

