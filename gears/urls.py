from django.urls import path
from . import views

urlpatterns = [
    path('', views.gears, name="gears"),
    path('<product_id>', views.gear_detail, name="gear_detail"),
]
