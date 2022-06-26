from rest_framework import serializers
from backend.models import Message
from backend.models import Idea

class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.username', read_only=True)
    post = serializers.CharField(source='post.title', read_only=True)
    
    class Meta:
       model = Message
       fields = ('sender',"content", "post")