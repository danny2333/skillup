from django import forms
from .models import TrainingPlan

class TrainingPlanForm(forms.ModelForm):
    class Meta:
        model = TrainingPlan
        fields = ['title', 'description', 'duration_weeks', 
                 'sessions_per_week', 'difficulty', 'drills']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
        }