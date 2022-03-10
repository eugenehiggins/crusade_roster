from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'armies'

# router = routers.DefaultRouter()
# router.register(r'armies', views.ArmiesViewSet)

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    path('', views.ArmyList.as_view()),
    path('<int:pk>/', views.ArmyDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
