from django.shortcuts import render
from .models import Book
from django.utils.datastructures import MultiValueDictKeyError


def index(request):
    try:
        print(request.GET['id'])
        
    except MultiValueDictKeyError:
        message = "You do not pass any data"

    finally:
        # print(request.method)
        # books = Book.objects.filter(price__lte=560)
        # books = Book.objects.all()
        books = Book.objects.get(id=1)
        
    
        context = {
            "name": "Khaled",
            "age": 78,
            "books": books,
        }
        try: 
            context["message"] = message
        except UnboundLocalError:
            pass
        return render(request, "index.html", context)