from django.contrib import admin
from django import forms
from .models import TrainingPlan

@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'difficulty', 'duration_weeks')
    
    # Just show all fields in simple text inputs
    fields = ('title', 'description', 'difficulty', 
              'duration_weeks', 'sessions_per_week', 'drills')