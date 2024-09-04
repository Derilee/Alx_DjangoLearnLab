from rest_framework import serializers
from .models import Book, Author
from datetime import datetime

#Author model is serialized here
class AuthorSerializer(serializers.Serializer):
    class Meta:
        model = Author
        fields = ['name']

#Book model is serialized here
class BookSerializer(serializers.Serializer):
    author_details = AuthorSerializer(read_only=True) #A new field is added here to handle relationships between the models by nesting the serializer

    class Meta:
        model = Book
        fields = ['__all__'] #all here means all the fields in the Book model including the author_details that is nested above

#we validate the publication year to make sure any year the user inputs isn't a future year
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Year can't be in the future")
        return value


