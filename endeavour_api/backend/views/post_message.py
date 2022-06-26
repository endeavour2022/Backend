import json
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Idea, User, Message

class PostMessage(APIView):
    
    def post(self, request):
        
        isAuthenticated = request.data.get("isAuthenticated", False)
        
        if not isAuthenticated:
            return Response({"error": "User is not authenticated"})
        
        result, is_valid = self.create(request.data)
        if is_valid:
            return Response({"message": "Message has been sent"})
        return Response({"error": result})
        
        
    def create(self, data):
        sender = data.get("sender", "")
        post = data.get("post", "")
        content = data.get("content", "")
        try:
            sender = User.objects.get(username=sender)
            post = Idea.objects.get(id=post)
        except:
            return "Failed to send", False
        
        message = Message.objects.create(sender=sender,
                            post=post,
                            content=content,
                            )
        
        message = message.save()
        return message, True