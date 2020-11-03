from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django import forms
from django.urls import reverse
import itertools

#Adding Favorite List
favorites = []

#Adding Complaint List
complaint_author = []
complaint_email = []
complaint_type = []
complaint_subject = []
complaint_message = []

class NewFavForm(forms.Form):
    new_favorite = forms.CharField(label="New Favorite", required="True")

class NewComplaintForm(forms.Form):
    name = forms.CharField(label="Your name:", max_length=100, required="True")
    sender = forms.EmailField(label="Your Email:", required="True")
    c_type = forms.CharField(label="Complaint Type:", required="True")
    subject = forms.CharField(label="Subject:", min_length=10, required="True")
    message = forms.CharField(label="Message:", max_length=300, required="True")


# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "Management/index.html", {
        "Favorites": favorites
    })

def view_fav(request):
    return render(request, "Management/Fav.html", {
        "favorites": favorites
    })

def add_fav(request):
    if request.method == "POST":
        form = NewFavForm(request.POST)
        if form.is_valid():
            new_favorite = form.cleaned_data["new_favorite"]
            favorites.append(new_favorite)
            return HttpResponseRedirect(reverse("Management:Add_Favourite"))
        else:
            return render(request, "Management/Add.html", {
                "form": form,
                "favorites": favorites
            })
    
    return render(request, "Management/Add.html", {
        "form": NewFavForm(),
        "favorites": favorites
    })

def add_complaint(request):
    if request.method == "POST":
        form = NewComplaintForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            sender=form.cleaned_data["sender"]
            c_type=form.cleaned_data["c_type"]
            subject=form.cleaned_data["subject"]
            message=form.cleaned_data["message"]
            complaint_author.append(name)
            complaint_email.append(sender)
            complaint_type.append(c_type)
            complaint_subject.append(subject)
            complaint_message.append(message)
            return HttpResponseRedirect(reverse("Management:Add_Complaint"))
        else:
            return render(request, "Management/add_complaint.html", {
                "form": form,
            })
    
    return render(request, "Management/add_complaint.html", {
        "form": NewComplaintForm()
    })

def view_complaint(request):
    return render(request, "Management/complaint.html", {
        "Complaint": zip(complaint_author, complaint_email, complaint_type, complaint_subject, complaint_message)
    })