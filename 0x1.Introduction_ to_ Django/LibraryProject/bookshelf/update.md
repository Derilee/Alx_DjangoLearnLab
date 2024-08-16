>>> from bookshelf.models import Book
>>> update_book = Book.objects.get(title = "1984")
>>> update_book.title = ("Nineteen Eighty-Four")
>>> update_book.save()
>>> 
>>> from bookshelf.models import Book
>>> all_books = Book.objects.all()
>>> for book in all_books:
...     print(f"{book.title}")
... 
Nineteen Eighty-Four