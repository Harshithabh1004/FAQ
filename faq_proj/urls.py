from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # Django admin interface
    path('api/', include('faq.urls')),  # Include FAQ app URLs
]