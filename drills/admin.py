# drills/admin.py
from django.contrib import admin
from .models import Drill

# Keep your existing Drill admin registration
admin.site.register(Drill)