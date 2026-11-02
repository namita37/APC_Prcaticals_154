"""URL configuration for login_project."""

from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # Redirect root to login
    path('', lambda request: redirect('login')),
]
