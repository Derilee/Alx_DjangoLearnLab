# query all books by a specific author
from relationship_app.models import Book, Author
book_author = Book.objects.filter()
for books in book_author:
    print(books.title)



# List all books in a library
from relationship_app.models import Library
all_libraries = Library.objects.all()
for library in all_libraries:
    all_books = library.books.all()
    print(f"library: {library}")
    for book in all_books:
        print(f"book:{book.title}")


# retrieve a librarian from a library
from relationship_app.models import Librarian
aLibrarian = Librarian.objects.get(name = "Librarian name")
print(f"Librarian: {aLibrarian.name}")
print(f"Library: {aLibrarian.library.name}")
