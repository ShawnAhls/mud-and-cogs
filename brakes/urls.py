from django.urls import path
from . import views

urlpatterns = [
    path('brakes/', views.brakes, name="brakes")
]
