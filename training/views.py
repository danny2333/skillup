from rest_framework import viewsets
from .models import Training
from .serializers import TrainingSerializer
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
class TrainingViewSet(viewsets.ModelViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer