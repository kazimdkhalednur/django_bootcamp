from django.urls import path
from django.views.generic import TemplateView, ListView
from .views import *


urlpatterns = [
    # path("", index),
    path("", BookListView.as_view(), name="index"),
    # path("", ListView.as_view(model=Book)),
    # path("about/", TemplateView.as_view(template_name="about.html")),
    path("about/", AboutView.as_view()),

    # path("<slug>/", detail_book, name="detail"),
    path("<slug>/", BookDetailView.as_view(), name="detail")
]