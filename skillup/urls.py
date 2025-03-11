from django.urls import path, include
from django.contrib import admin
from django.urls import path
from community.views import home
from django.conf.urls.static import static
from django.conf import settings
from users.views import register ,user_login


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('drills.urls')), 
    path('api/', include('training.urls')), 
    path('api/', include('community.urls')),  
    path('api/', include('users.urls')),  
    path('', include('community.urls')),  
    path('register/', register, name='register'),
     path('login/', user_login, name='login'), 
    path('drills/', include('drills.urls')),  
    path('training/', include('training.urls')),
    path('users/', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
