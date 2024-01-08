from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("categories/<str:category_name>", views.category, name="category"),
    path("search", views.search, name="search"),
    path("search?q=<str:query>", views.search_query, name="search_query"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("contact", views.contact, name="contact")
]