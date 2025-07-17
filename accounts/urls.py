"""
Конечные точки API приложения `accounts`.
"""
from django.urls import path
from rest_framework.routers import DefaultRouter

from accounts.apps import AccountsConfig
from accounts.views import UserModelViewSet


router = DefaultRouter()
router.register(r"", UserModelViewSet, basename="user")
app_name = AccountsConfig.name
urlpatterns = [
    path('me/', UserModelViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update'
    }), name='user-me'),
]
urlpatterns += router.urls
