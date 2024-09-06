The AuthorListView is configured to create new authors or list existing authors

AuthorDetailView is configured to retrieve,update or destroy an author from the author model using the private key

BookListView is configured to list all books in the book model and it can be accessed by authenticated and non authenticated users

BookDetailView is configured to give a detailed list of one book. it can be accessed using the private key

BookCreateView is configured to enable only authenticated users to be able to create new book. this settings is modified through the perform_create method

BookUpdateView is configured to enable only authenticated users to be able to update existing book through it's private key. this settings is modified through the perform_update method

BookDeleteView is configured to enable only authenticated users to be able to delete an existing book through it's private key. this settings is modified through the perform_delete method 