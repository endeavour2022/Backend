from rest_framework import serializers
from backend.models import Workshop

class WorkshopSerializer(serializers.ModelSerializer):
    mentor = serializers.CharField(source="mentor.first_name", read_only=True)
    
    class Meta:
       model = Workshop
       fields = "__all__"