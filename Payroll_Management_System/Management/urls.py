from django.urls import path
from . import views


app_name = "Management"
urlpatterns=[
    path("", views.index, name="Index"),
    path("Fav/", views.Fav, name="Fav"),
    path("<str:name>", views.Greet, name="Greet"),
    path("add/", views.addFav, name="AddFav"),
    path("addcompl/", views.addComp, name="AddComp"),
    path("complaints/", views.View_Complaint, name="complaint")
]