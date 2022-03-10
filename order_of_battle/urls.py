from django.urls import path, include
from rest_framework import routers

from . import views

app_name = 'armies'

# router = routers.DefaultRouter()
# router.register(r'armies', views.ArmiesViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    path('', views.army_list),
    path('<int:pk>/', views.army_detail),
]