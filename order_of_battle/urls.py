from django.urls import path, include
from rest_framework import routers

from . import views

# app_name = 'armies'

router = routers.DefaultRouter()
router.register(r'armies', views.ArmiesViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    path('api/', include('rest_framework.urls', namespace='rest_framework'))
]