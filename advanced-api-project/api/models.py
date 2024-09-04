from django.db import models

# Author model is created here with the name field
class Author(models.Model):
    name = models.CharField(max_length=200)


#Book model is created here with its field
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE) #author is referenced to the Author model as a foreign key. in this case, it shows one to many relationship which means a book can have only one author but one author can author many books

