from django import forms
from .models import Book


# class BookCreateForm(forms.Form):
#     title = forms.CharField()
#     price = forms.DecimalField()
#     discount_price = forms.DecimalField()
#     quantity = forms.IntegerField()


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = ["title", "price", "discount_price", "quantity"]
        # fields = "__all__"
        exclude = ["is_active"]