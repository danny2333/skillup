from django.urls import path
from . import views

app_name = 'training'  # Add this for namespace

urlpatterns = [
    path('', views.training_plan_list, name='training_list'),
    path('add/', views.add_training, name='add_training'),
    path('<int:pk>/', views.plan_detail, name='plan_detail'), 
]