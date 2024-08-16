>>> from bookshelf.models import Book
>>> retrieve_book = Book.objects.all()
>>> for book in retrieve_book:
...     print(f"Title: {book.title}")
...     print(f"Author: {book.author}")
...     print(f"Publication Year: {book.publication_year}")
...     
... 
Title: 1984
Author: George Orwell
Publication Year: 1949