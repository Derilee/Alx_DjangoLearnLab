The AuthorListView is configured to create new authors or list existing authors

AuthorDetailView is configured to retrieve,update or destroy an author from the author model using the private key

BookListView is configured to list all books in the book model and it can be accessed by authenticated and non authenticated users

BookDetailView is configured to give a detailed list of one book. it can be accessed using the private key

BookCreateView is configured to enable only authenticated users to be able to create new book. this settings is modified through the perform_create method

BookUpdateView is configured to enable only authenticated users to be able to update existing book through it's private key. this settings is modified through the perform_update method

BookDeleteView is configured to enable only authenticated users to be able to delete an existing book through it's private key. this settings is modified through the perform_delete method 


To test how the filtering works, go to - http://127.0.0.1:8000/api/books/?author=1 or replace the author with publication_year if you are filtering by publication year and not author id


To test how the search works, go to - http://127.0.0.1:8000/api/books/?search=fire
(fire in this case is my book title)


To test how the order works, go to, http://127.0.0.1:8000/api/books/?ordering=-title