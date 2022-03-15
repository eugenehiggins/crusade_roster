from django.urls import path, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

# app_name = 'armies'

# router = routers.DefaultRouter()
# router.register(r'armies', views.ArmiesViewSet)

urlpatterns = format_suffix_patterns([
    # path('', views.index, name='index'),
    # path('<int:id>/', views.detail, name='detail'),
    # path('', views.ArmyList.as_view()),
    path('', views.api_root),
    path('armies/', views.ArmyList.as_view(), name='army-list'),
    path('armies/<int:pk>/', views.ArmyDetail.as_view(), name='army-detail'),
    path('users/',
         views.UserList.as_view(),
         name='user-list'),
    path('users/<int:pk>/',
         views.UserDetail.as_view(),
         name='user-detail')
])

# urlpatterns = format_suffix_patterns(urlpatterns)
