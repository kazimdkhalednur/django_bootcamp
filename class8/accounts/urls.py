from django.urls import path
from .views import signup, login, index, logout


urlpatterns = [
    path("signup/", signup),
    path("login/", login),
    path("index/", index, name="index"),
    path("logout1/", logout, name="logout")
]