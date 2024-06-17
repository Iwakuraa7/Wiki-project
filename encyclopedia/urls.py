from django.urls import path

from . import views

#  TODO: create_new_page function is not working as planned, it can't append new url to urlpatterns.
#  TODO: It seems that the functions, for creating new pages, are meant to be defined in views.py
#  TODO: Nevertheless, create_new_page func,
#   in terms of parsing the input from the user and creating both md and html file from it, works without hesitation

urlpatterns = [
    path("", views.index, name="index"),
    path("CSS", views.CSS_entry, name="CSS"),
    path("Django", views.Django_entry, name="Django"),
    path("Git", views.Git_entry, name="Git"),
    path("HTML", views.HTML_entry, name="HTML"),
    path("Python", views.Python_entry, name="Python"),
    path("Create", views.create_new_page, name="create_new_page"),
    path("<str:title>", views.dynamic_entry, name="dynamic_entry")
]