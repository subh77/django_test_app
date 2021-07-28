from typing import Counter
from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path("", views.index_a1, name="index_a1"),
    path("counter", views.counter_a1, name="counter_a1"),
]
