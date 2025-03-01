from django.db import models

class Training(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()  # Duration in minutes
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name