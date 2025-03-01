from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TrainingViewSet

router = DefaultRouter()
router.register(r'trainings', TrainingViewSet)

urlpatterns = [
    path('', include(router.urls)),
]