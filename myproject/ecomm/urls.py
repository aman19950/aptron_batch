from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [

    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("save/", views.save, name="save"),
    path("login/", views.login, name="login"),


    path("register", views.register, name="register"),
    path("login_info", views.login_info, name="login_info"),
    path("logout", views.logout, name="logout"),
    path("sc", views.sc, name="sc")

]
