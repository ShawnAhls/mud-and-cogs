from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('gears/', include('gears.urls')),
    path('brakes/', include('brakes.urls')),
    path('tires/', include('tires.urls')),
    path('basket/', include('basket.urls')),
]
