from django.urls import path
from .views import register, user_login, user_logout, profile, edit_profile

urlpatterns = [
    path('logout/', user_logout, name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_profile, name='edit_profile'),
]