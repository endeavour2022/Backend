from django.db import models

ROLE_CHOICES = [("investor", "investor"),("entrepreneur", "entrepreneur"), ("mentor", "mentor")]
    
class User(models.Model):
    
    first_name = models.CharField(max_length=256, blank=True, null=True, default="")
    last_name = models.CharField(max_length=256, blank=True, null=True, default="")
    username = models.CharField(max_length=50, unique=True, null=True, blank=True, default="")
    phone = models.CharField(max_length=20, null=True, blank=True, default="")
    linkedin_link = models.CharField(max_length=50, null=True, blank=True, default="")
    role =  models.CharField(max_length=20, choices=ROLE_CHOICES, default="entrepreneur", null=True, blank=True)
    photo = models.ImageField(upload_to='images/', null=True, blank=True, default="")
    bio = models.CharField(max_length=1000,null=True, blank=True, default="")
    joining_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    designation = models.CharField(max_length=50, null=True, blank=True, default="")
    city = models.CharField(max_length=100, null=True, blank=True, default="")
    email = models.EmailField(null=True, blank=True, default="")
    projects = models.CharField(max_length=1000, null=True, blank=True, default="")
    year_of_experience = models.IntegerField(blank=True, default=1)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    password = models.CharField(max_length=200, null=False, blank=False, default="1234")
    verification_code = models.IntegerField(null=True, blank=True, default=000000)
    
    REQUIRED_FIELDS = []
    USERNAME_FIELD = ("username")
    
    def __str__(self):
        return self.username
    
    def save(self, *args, **kwargs):
        self.full_clean()
        return super().save(*args, **kwargs)
