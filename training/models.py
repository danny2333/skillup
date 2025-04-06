# training/models.py
from django.db import models
from drills.models import Drill

class TrainingPlan(models.Model):
    title = models.CharField(max_length=100)  # Ensure this exists
    description = models.TextField()
    duration_weeks = models.PositiveIntegerField(default=4)
    sessions_per_week = models.PositiveIntegerField(default=3)
    difficulty = models.CharField(max_length=20, choices=[
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced')
    ])
    drills = models.ManyToManyField(Drill)