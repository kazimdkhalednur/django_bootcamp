from collections.abc import Iterable
import uuid
from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class PublishedBookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status="published")


class Book(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    author = models.CharField(max_length=100)
    slug = models.SlugField(blank=True)
    STATUS_CHOICE = (
        ("draft", "Draft htrh"),
        ("published", "Published"),
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICE, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    objects = models.Manager()
    published_objects = PublishedBookManager()

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_book_url(self):
        return reverse("detail", kwargs={"slug": self.slug})
    

class Book2(models.Model):
    id = models.UUIDField(primary_key=True, blank=True, unique=True, editable=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            self.id = uuid.uuid4()
        super().save(*args, **kwargs)