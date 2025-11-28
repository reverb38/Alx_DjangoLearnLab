# api/models.py
from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200, blank=True, null=True)
    author = models.CharField(max_length=100, blank=True, null=True)
    published_date = models.DateField(null=True, blank=True)
    isbn = models.CharField(max_length=13, unique=True, blank=True, null=True)
    pages = models.IntegerField(null=True, blank=True)
    cover = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title or "Untitled Book"
