from django.urls import path
from . import views

urlpatterns = [
    path('', views.brakes, name="brakes")
]
