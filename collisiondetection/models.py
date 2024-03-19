from django.db import models

# Create your models here.
class ObstacleDetectionEvent(models.Model):
    timestamp = models.DateTimeField(auto_now_add = True)
    description = models.TextField(blank=True, null=True)