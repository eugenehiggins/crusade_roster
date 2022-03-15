from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# app_name = 'armies'

# router = routers.DefaultRouter()
# router.register(r'armies', views.ArmiesViewSet)
from order_of_battle.views import ArmyViewSet, UserViewSet

army_list = ArmyViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

army_detail = ArmyViewSet.as_view({
    'get': 'retreieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy',
})

user_list = UserViewSet.as_view({
    'get': 'list'
})

user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('', views.ArmyList.as_view()),
    path('', views.api_root),
    path('armies/', army_list, name='army-list'),
    path('armies/<int:pk>/', army_detail, name='army-detail'),
    path('users/', user_list, name='user-list'),
    path('users/<int:pk>/', user_detail, name='user-detail')
])

# urlpatterns = format_suffix_patterns(urlpatterns)
