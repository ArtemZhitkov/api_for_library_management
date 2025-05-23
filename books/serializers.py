from rest_framework import serializers

from books.models import Book, Genre, Category
from author.serializers import AuthorSerializers


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class GenreSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Genre
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializers(read_only=True)
    genre = GenreSerializer(read_only=True)

    class Meta:
        model = Book
        fields = "__all__"
