from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django import forms

Favorites = ["foo", "bar", "baz"]

class NewTaskForm(forms.Form):
    Fav = forms.CharField(label="New Favorite")



# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "Management/index.html", {
        "newyear": now.month == 10 and now.day == 3
    })

def Greet(request, name):
    return render(request, "Management/greet.html", {
        "name": name.capitalize()
    })

def Fav(request):
    return render(request, "Management/Fav.html", {
        "Favorites": Favorites
    })

def add(request):
    if request.method=="POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            form.cleaned_data["Fav"]
    return render(request, "Management/Add.html", {
        "form": NewTaskForm()
    })