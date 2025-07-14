"""
Конечные точки API приложения `accounts`.
"""

from rest_framework.routers import DefaultRouter

from .apps import AccountsConfig
from .views import UserModelViewSet

router = DefaultRouter()
router.register(r"users", UserModelViewSet, basename="user")

app_name = AccountsConfig.name

urlpatterns = router.urls
