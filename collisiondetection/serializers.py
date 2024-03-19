from rest_framework import serializers
from collisiondetection.models import ObstacleDetectionEvent

#Serializers

class ObstacleDetectionEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObstacleDetectionEvent
        fields = ['timestamp','description']
