from django.urls import path
from . import views

urlpatterns = [
    path('tires/', views.tires, name="tires")
]
