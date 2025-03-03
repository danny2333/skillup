from django.urls import path
from .views import community_list, add_post, home

urlpatterns = [
    path('', home, name='home'),
    path('community/', community_list, name='community_list'),
    path('community/add/', add_post, name='add_post'),
]