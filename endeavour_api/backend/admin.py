from django.contrib import admin
from backend.models import User, Idea, Workshop, Message

admin.site.register(User)
admin.site.register(Idea)
admin.site.register(Workshop)
admin.site.register(Message)

# Register your models here.
