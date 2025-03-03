from django.shortcuts import render, redirect
from .models import TrainingPlan
from .forms import TrainingPlanForm

def training_list(request):
    plans = TrainingPlan.objects.all()
    return render(request, 'training/training_list.html', {'plans': plans})

def add_training(request):
    if request.method == 'POST':
        form = TrainingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingPlanForm()
    return render(request, 'training/add_training.html', {'form': form})