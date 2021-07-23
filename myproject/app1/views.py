from os import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        "name": "Subh",
        "age": 26,
        "nationality": "Indian",
    }
    return render(request, "index.html", context)
