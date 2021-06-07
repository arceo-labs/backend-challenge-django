from django.conf import settings
from rest_framework.routers import DefaultRouter

from api import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

# For example:
# router.register(r'subscription', views.SubscriptionViewSet)
