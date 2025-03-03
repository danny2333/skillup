from django.urls import path
from .views import drill_list, add_drill

urlpatterns = [
    path('', drill_list, name='drill_list'),
    path('add/', add_drill, name='add_drill'),
]