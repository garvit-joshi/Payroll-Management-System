from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "Management/index.html")

def Greet(request, name):
    return render(request, "Management/greet.html", {
        "name": name.capitalize()
    })