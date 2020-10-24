from django.db import models

from config import settings


class Book(models.Model):
    name = models.CharField(max_length=200)
    sub_name = models.CharField(max_length=200)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    description = models.TextField()
    published_date = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
