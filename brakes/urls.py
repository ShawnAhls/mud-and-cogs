# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('brakes/', views.index, name="brakes")
]
