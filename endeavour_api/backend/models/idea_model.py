from django.db import models
from backend.models import User


STATUS_CHOICES = [("active", "active"),("pending", "pending"), ("rejected", "rejected")]

class Idea(models.Model):
    
    title = models.TextField(max_length=500, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    category = models.CharField(max_length=50, blank=True, null=True)
    funds = models.IntegerField(blank=True, null=True)
    video = models.CharField(max_length=500, null=True, blank=True)
    documents = models.CharField(max_length=500, null=True, blank=True)
    start_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending", null=True, blank=True)
    likes = models.IntegerField(blank=True, null=True, default=1)
    approved_by = models.CharField(max_length=100,blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)