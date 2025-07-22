"""
Конечные точки API.
"""
from django.urls import path
from rest_framework.routers import DefaultRouter

from .apps import HabitsConfig
from .views import HabitModelViewSet, health_check

app_name = HabitsConfig.name
router = DefaultRouter()
router.register(r"habits", HabitModelViewSet, basename="habit")

urlpatterns = [
    path("health/", health_check, name="health-check")
]

urlpatterns += router.urls
