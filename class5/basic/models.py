from django.db.models import Model
from django.db import models


class Author(Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Book(Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    id = models.AutoField(primary_key=True, unique=True)
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    price = models.FloatField()
    created_at = models.DateField(blank=False, null=True)

    def __str__(self):
        return self.title
    



