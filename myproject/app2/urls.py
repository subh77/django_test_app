from typing import Counter
from django.urls import path
from . import views

app_name = "app2"

urlpatterns = [
    path("", views.index, name="index"),
    path("counter", views.counter, name="counter"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("post/<str:pk>", views.post, name="post"),
]
