from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['name', 'title']


    # def validate(self, data):
    #     if data(len('author' < 5)):
    #         raise serializers.ValidationError("author must be 5 characters long")
    #     return data
