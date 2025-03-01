from rest_framework import viewsets
from .models import Community
from .serializers import CommunitySerializer
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

class CommunityViewSet(viewsets.ModelViewSet):
    queryset = Community.objects.all()
    serializer_class = CommunitySerializer