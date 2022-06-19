import json
import random
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Idea
from backend.models import User

class CreateIdea(APIView):
    
    def post(self, request):
        
        username = request.data.get("username", None)
        
        if not username:
            return Response({"error": "Provide a username"})
        
        if not User.objects.filter(username=username).exists():
            return Response({"error": "Provide a valid username"})
        
        result, is_valid = self.create(request.data)
        return Response({"message": "Idea has been submitted"})
        
        
    def create(self, data):
        title = data.get("title", "")
        description = data.get("description", "")
        category = data.get("category", "")
        funds = data.get("funds", 10000)
        video = data.get("video", "")
        documents = data.get("documents", "")
        start_date = data.get("start_date", "")
        status = data.get("status", "pending")
        clicks = data.get("clicks", 1)
        impressions = data.get("impressions", 1)
        creator = User.objects.get(username=data["username"])
        
        idea = Idea.objects.create(title=title,
                            description=description,
                            category=category,
                            funds=funds,
                            documents=documents,
                            video=video,
                            start_date=start_date,
                            status=status,
                            clicks=clicks,
                            impressions=impressions,
                            creator=creator)
        
        idea = idea.save()
        return idea, True