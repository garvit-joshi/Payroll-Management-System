from django.urls import path
from . import views


app_name = "Management"
urlpatterns=[
    path("", views.index, name="Home"),
    path("fav/", views.view_fav, name="View_Favourite"),
    path("addfav/", views.add_fav, name="Add_Favourite"),
    path("addcompl/", views.add_complaint, name="Add_Complaint"),
    path("compl/", views.view_complaint, name="View_Complaint"),
    path("search/", views.search, name="Search"),
    path("signup/", views.sign_up, name="Sign_Up")
]