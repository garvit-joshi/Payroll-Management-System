from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django import forms
from django.urls import reverse

Favorites = []

class NewTaskForm(forms.Form):
    Fav = forms.CharField(label="New Favorite")



# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "Management/index.html", {
        "Favorites": Favorites
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
            Fav=form.cleaned_data["Fav"]
            Favorites.append(Fav)
            return HttpResponseRedirect(reverse("Management:Add"))
        else:
            return render(request, "Management/Add.html", {
                "form": form,
                "Favorites": Favorites
            })
    
    return render(request, "Management/Add.html", {
        "form": NewTaskForm(),
        "Favorites": Favorites
    })