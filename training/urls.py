from django.urls import path
from .views import training_list, add_training

urlpatterns = [
    path('', training_list, name='training_list'),
    path('training/add/', add_training, name='add_training'),
]