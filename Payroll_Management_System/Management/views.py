from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django import forms
from django.urls import reverse
import itertools

#Adding Favorite List
Favorites = []

#Adding Complaint List
CompType = []
CompSubject = []
CompMessage = []
CompAuthor = []
CompEmail = []

class NewFavForm(forms.Form):
    Fav = forms.CharField(label="New Favorite", required="True")

class NewComplaintForm(forms.Form):
    name = forms.CharField(label="Your name:", max_length=100, required="True")
    sender = forms.EmailField(label="Your Email:", required="True")
    Comptype = forms.CharField(label="Complaint Type:", required="True")
    subject = forms.CharField(label="Subject:", min_length=10, required="True")
    message = forms.CharField(label="Message:",max_length=300, required="True")


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

def addFav(request):
    if request.method=="POST":
        form = NewFavForm(request.POST)
        if form.is_valid():
            Fav=form.cleaned_data["Fav"]
            Favorites.append(Fav)
            return HttpResponseRedirect(reverse("Management:AddFav"))
        else:
            return render(request, "Management/Add.html", {
                "form": form,
                "Favorites": Favorites
            })
    
    return render(request, "Management/Add.html", {
        "form": NewFavForm(),
        "Favorites": Favorites
    })

def addComp(request):
    if request.method=="POST":
        form = NewComplaintForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            sender=form.cleaned_data["sender"]
            Comptype=form.cleaned_data["Comptype"]
            subject=form.cleaned_data["subject"]
            message=form.cleaned_data["message"]
            CompAuthor.append(name)
            CompType.append(Comptype)
            CompEmail.append(sender)
            CompMessage.append(message)
            CompSubject.append(subject)
            return HttpResponseRedirect(reverse("Management:AddComp"))
        else:
            return render(request, "Management/add_complaint.html", {
                "form": form,
            })
    
    return render(request, "Management/add_complaint.html", {
        "form": NewComplaintForm()
    })

def View_Complaint(request):
    return render(request, "Management/complaint.html", {
        "Complaint":zip(CompAuthor,CompEmail,CompType,CompSubject,CompMessage)
    })