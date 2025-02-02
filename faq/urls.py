from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet

# Create a router and register the FAQViewSet
router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

# Define the URL patterns
urlpatterns = [
    path('', include(router.urls)),  # Include all routes from the router
]