from django.urls import path
from . import views

urlpatterns = [
    path('parts/', views.parts, name="parts")
]
