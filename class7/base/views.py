from django.shortcuts import render
from .forms import BookCreateForm
from .models import Book


def create_book(request):
    if request.method == "POST":
        form = BookCreateForm(data=request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # book = Book(title=form.cleaned_data["title"], 
            #             price=form.cleaned_data["price"], 
            #             discount_price=form.cleaned_data["discount_price"],
            #             quantity=form.cleaned_data["quantity"])
            # book.save()
            # Book.objects.create(title=form.cleaned_data["title"], 
            #             price=form.cleaned_data["price"], 
            #             discount_price=form.cleaned_data["discount_price"],
            #             quantity=form.cleaned_data["quantity"])
            book = form.save()
            book.is_active = False
            book.save()
            return render(request, 'success.html')
        
    else:
        form = BookCreateForm()
        context = {
            "form": form
        }
        return render(request, 'create_book.html', context)
