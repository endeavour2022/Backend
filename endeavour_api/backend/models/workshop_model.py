from django.db import models
from numpy import blackman
from backend.models import User


STATUS_CHOICES = [("active", "active"),("pending", "pending"), ("rejected", "rejected")]

class Workshop(models.Model):
    
    title = models.TextField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    about = models.TextField(max_length=1000, blank=True, null=True)
    charges = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", null=True, blank=True)
    picture = models.CharField(null=True, blank=True, max_length=500)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)