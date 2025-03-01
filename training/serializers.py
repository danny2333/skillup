from rest_framework import serializers
from .models import Training

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ['id', 'name', 'description', 'duration', 'created_at']