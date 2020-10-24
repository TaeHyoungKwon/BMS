from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)


class Book(models.Model):
    name = models.CharField(max_length=200)
    sub_name = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
