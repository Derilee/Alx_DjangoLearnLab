>>> from bookshelf.models import Book
>>> delete_book = Book.objects.get(title = "Nineteen Eighty-Four")
>>> delete_book.delete()
(1, {'bookshelf.Book': 1})
>>> from bookshelf.models import Book
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(f"{book.title}")
...     print(f"{book.author}")
...     print(f"{book.publication_year}")
... 
>>> 
>>> 