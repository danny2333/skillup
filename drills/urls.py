from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DrillViewSet

router = DefaultRouter()
router.register(r'drills', DrillViewSet)

urlpatterns = [
    path('', include(router.urls)),
]