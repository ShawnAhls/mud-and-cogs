from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('gears.urls')),
    path('', include('brakes.urls')),
    path('', include('tires.urls')),
]
