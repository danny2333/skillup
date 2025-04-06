from django.shortcuts import render, redirect
from .models import Drill
from .forms import DrillForm

def drill_list(request):
    drills = Drill.objects.all()  # Get all drills from the database
    return render(request, 'drills/drill_list.html', {'drills': drills})

def add_drill(request):
    if request.method == 'POST':
        form = DrillForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new drill to the database
            return redirect('drill_list')  # Go back to the drills list
    else:
        form = DrillForm()
    return render(request, 'drills/add_drill.html', {'form': form})
