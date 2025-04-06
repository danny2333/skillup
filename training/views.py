from django.shortcuts import render, redirect, get_object_or_404
from .models import TrainingPlan
from .forms import TrainingPlanForm

def training_plan_list(request):
    plans = TrainingPlan.objects.all()
    return render(request, 'training/plan_list.html', {'plans': plans})

def plan_detail(request, pk):  # Add this new view
    plan = get_object_or_404(TrainingPlan, pk=pk)
    return render(request, 'training/plan_detail.html', {'plan': plan})

def add_training(request):
    if request.method == 'POST':
        form = TrainingPlanForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('training_list')
    else:
        form = TrainingPlanForm()
    return render(request, 'training/add_plan.html', {'form': form})