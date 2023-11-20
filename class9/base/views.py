from django.shortcuts import render
from .models import Book
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib import messages


# def index(request):
#     books = Book.objects.all()
#     context = {
#         "books":books
#     }
#     return render(request, "index.html", context)


class BookListView(ListView):
    model = Book
    template_name="index.html"


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
