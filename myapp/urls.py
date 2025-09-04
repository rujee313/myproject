from django.contrib import admin
from django.urls import path, include  # include is needed to connect app URLs

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin panel
    path('', include('accounts.urls')),  # Your app's URLs (signup)
    path('accounts/', include('django.contrib.auth.urls')),  # built-in login/logout
]
