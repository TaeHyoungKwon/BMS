from django.db import models

from book.constants import BOOK_TYPE, NEW_BOOKS


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=200)
    sub_name = models.CharField(max_length=200, blank=True)
    type = models.CharField(max_length=30, choices=BOOK_TYPE, default=NEW_BOOKS)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=0, blank=True, default=0)
    sale_price = models.DecimalField(
        max_digits=5, decimal_places=0, blank=True, default=0
    )
    purchased_at = models.DateField(null=True)
    published_at = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
