from django.urls import path
from . import views

urlpatterns = [
    path('', views.purchase, name="purchase"),
    path('purchase_successful/<purchase_number>',
         views.purchase_successful, name="purchase_successful")
]
