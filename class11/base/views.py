from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Book, Book2
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages

from django.views.decorators.cache import cache_page
from django.core.paginator import Paginator


# @cache_page(60*2)
def index(request):
    print("in View")
    # books = Book.objects.filter(price__gt=30)
    # count = Book.objects.count()
    books = Book.objects.all()

    size = request.GET["size"]
    paginator = Paginator(books, size)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    print(page_obj.paginator.num_pages)

    context = {
        "books":page_obj,
        # "count": count
    }
    return render(request, "index.html", context)


# class BookListView(ListView):
#     model = Book
#     template_name="index.html"

#     def get_queryset(self):
#         return Book.published_objects.all().order_by("-updated_at")


def detail_book(request, slug):
    book = Book.objects.filter(slug=slug)
    if book.exists():
        book = Book.objects.get(slug=slug)
        context = {
            "book":book
        }
        return render(request, "book.html", context)
    messages.error(request, "Book not found")
    return render(request, "book.html")

class BookDetailView(DetailView):
    model = Book
    # pk = "slug"

class AboutView(TemplateView):
    template_name="about.html"
