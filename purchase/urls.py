from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.purchase, name="purchase"),
    path('purchase_successful/<purchase_number>',
         views.purchase_successful, name="purchase_successful"),
    path('wh/', webhook, name="webhook"),
]
