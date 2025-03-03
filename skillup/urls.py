from django.urls import path, include
from django.contrib import admin
from django.urls import path
from community.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drills.urls')), 
    path('api/', include('training.urls')), 
    path('api/', include('community.urls')),  
    path('api/', include('users.urls')),  
    path('', include('community.urls')),  
    path('drills/', include('drills.urls')),  
    path('training/', include('training.urls')),
    path('users/', include('users.urls')),
]
