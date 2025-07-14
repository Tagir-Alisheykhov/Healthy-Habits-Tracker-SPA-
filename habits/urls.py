"""
Конечные точки API.
"""

from rest_framework.routers import DefaultRouter

from .apps import HabitsConfig
from .views import HabitModelViewSet

app_name = HabitsConfig.name
router = DefaultRouter()
router.register(
    r"habits",
    HabitModelViewSet,
    basename="habit"
)
urlpatterns = router.urls
