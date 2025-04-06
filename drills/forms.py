from django import forms
from .models import Drill

class DrillForm(forms.ModelForm):
    class Meta:
        model = Drill
        fields = ['name', 'description', 'video_url']

class CommunityPostForm(forms.Form):
    # Your form fields here
    title = forms.CharField(max_length=100)
    content = forms.CharField(widget=forms.Textarea)
    # ... other fields