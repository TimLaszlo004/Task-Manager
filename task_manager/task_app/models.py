from django.db import models

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    due_at = models.DateTimeField()
    status = models.CharField(max_length=255, default="pending")
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['due_at']