from os import name
from django.shortcuts import render
from django.http import HttpResponse
from .models import Features

# Create your views here.
def index(request):
    feature = Features.objects.all()
    return render(request, "index.html", {"feature": feature})


def counter(request):
    words = request.POST["words"]
    word_counter = len(words.split())
    return render(request, "counter.html", {"count": word_counter})
