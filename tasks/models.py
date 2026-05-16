# Create your models here.
from django.db import models

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Baixa'),
        ('MED', 'Média'),
        ('HIGH', 'Alta'),
    ]
        
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    priority = models.CharField(
        max_length=4, 
        choices=PRIORITY_CHOICES, 
        default='MED'
        )
    is_done = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title