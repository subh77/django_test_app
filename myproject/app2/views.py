from os import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")


def counter(request):
    words = request.POST["words"]
    word_counter = len(words.split())
    return render(request, "counter.html", {"count": word_counter})
