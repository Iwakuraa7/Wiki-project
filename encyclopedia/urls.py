from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("CSS", views.CSS_entry, name="CSS"),
    path("Django", views.Django_entry, name="Django"),
    path("Git", views.Git_entry, name="Git"),
    path("HTML", views.HTML_entry, name="HTML"),
    path("Python", views.Python_entry, name="Python"),
    path("Create", views.create_new_page, name="create_new_page"),
    path("Edit", views.edit_page, name="edit_page"),
    path("Save", views.save_edit_page, name="save_edit_page"),
    path("Random_page", views.random_page, name="random_page"),
    path("<str:title>", views.dynamic_entry, name="dynamic_entry")
]
