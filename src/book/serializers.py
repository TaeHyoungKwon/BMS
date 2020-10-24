from rest_framework import serializers

from book.models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "name",
            "sub_name",
            "type",
            "author",
            "description",
            "price",
            "sale_price",
            "purchased_at",
            "published_at",
            "created_at",
            "updated_at",
        ]
