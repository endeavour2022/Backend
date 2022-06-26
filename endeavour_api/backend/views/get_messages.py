from ast import ExtSlice
from email import message
import json
import random
from re import I
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import User, Message
from backend.serializers import MessageSerializer

class GetMessage(APIView):
    
    def post(self, request):
        
        isAuthenticated = request.data.get("isAuthenticated", False)
        username = request.data.get("username", 'sample')
        
        if not isAuthenticated:
            return Response({"error": "User is not authenticated"})
        if not username:
            return Response({"error", "Enter username"})
        try:
            user = User.objects.get(username=username)
            messages = Message.objects.filter(post__creator=user)    
            all_messages = MessageSerializer(messages, many=True)
            return Response({"result": all_messages.data})
        except:
            return Response({"alert": "No result found"})

