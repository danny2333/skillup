from django import forms
from .models import Drill

class DrillForm(forms.ModelForm):
    class Meta:
        model = Drill
        fields = ['name', 'description', 'video_url']