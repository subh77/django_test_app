from typing import Counter
from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path("", views.index, name="index"),
    path("counter", views.counter, name="counter"),
]
