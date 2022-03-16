from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

# app_name = 'armies'

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'armies', views.ArmyViewSet)
router.register(r'users', views.UserViewSet)

# the API URLs are now determined automatically by the router.
urlpatterns = [
    path('', include(router.urls))
]