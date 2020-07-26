from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('purchase/', include('purchase.urls')),
    path('basket/', include('basket.urls')),
    path('register/', include('register.urls')),
    path('signin/', include('signin.urls')),
    path('parts/', include('parts.urls')),
    path('accounts/', include('allauth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
