from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="Index"),
    path("about", views.about, name="about"),
    path("categories", views.categories, name="categories"),
    path("login", views.login, name="login"),
    path("signup", views.signup, name="signup"),
    path("blogpost/<int:id>", views.blogpost, name="BlogPost")
]
