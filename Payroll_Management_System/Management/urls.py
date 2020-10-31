from django.urls import path
from . import views


app_name = "Management"
urlpatterns=[
    path("", views.index, name="Index"),
    path("Fav/", views.Fav, name="Fav"),
    path("<str:name>", views.Greet, name="Greet"),
    path("add/", views.add, name="Add")
]