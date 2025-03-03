from django.shortcuts import render, redirect
from .models import Drill
from .forms import DrillForm

def drill_list(request):
    drills = Drill.objects.all()
    return render(request, 'drills/drill_list.html', {'drills': drills})

def add_drill(request):
    if request.method == 'POST':
        # Handle form submission
        pass
    else:
        # Display the form
        return render(request, 'drills/add_drill.html')