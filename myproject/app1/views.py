from os import name
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_a1(request):
    return render(request, "index_a1.html")


def counter_a1(request):
    words = request.POST["words"]
    word_counter = len(words.split())
    return render(request, "counter_a1.html", {"count": word_counter})
