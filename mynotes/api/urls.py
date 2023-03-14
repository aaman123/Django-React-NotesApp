from django.urls import path
from .import views

urlpatterns = [
  path("", views.getRoutes, name = "getRoutes"),
  path("healthCheck/", views.getHealth, name = "getHealth"),
  path("notes/", views.getNotes, name = "getNotes"),
  path("note/<pk>/", views.getNote, name = "getNote"),
  path("saveNote/", views.postNote, name = "postNote")
]