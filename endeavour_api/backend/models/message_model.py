from statistics import mode
from django.db import models
from backend.models import User, Idea

class Message(models.Model):
    
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Idea, on_delete=models.CASCADE)
    content = models.CharField(max_length=1000, null=True, blank=True)
    time = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.post.title
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)