from django.db import models

class Drill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.name
    