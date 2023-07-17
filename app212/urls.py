from django.contrib import admin
from django.urls import path, include
from app212 import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blogpost/<str:slug>/", views.blogpost, name="blogpost"),
]
