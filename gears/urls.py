from django.urls import path
from . import views

urlpatterns = [
    path('', views.gears, name="gears"),
    # path('<gear_id>', views.gear_detail, name="gear_detail"),
]
