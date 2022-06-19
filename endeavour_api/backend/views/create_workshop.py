import json
import random
from requests import request
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Idea, User, Workshop

class CreateWorkshop(APIView):
    
    def post(self, request):
        
        username = request.data.get("username", None)
        
        if not username:
            return Response({"error": "Provide a username"})
        
        if not User.objects.filter(username=username).exists():
            return Response({"error": "Provide a valid username"})
        
        result, is_valid = self.create(request.data)
        return Response({"message": "Workshop has been created"})
        
        
    def create(self, data):
        title = data.get("title", "")
        description = data.get("description", "")
        about = data.get("about", "")
        charges = data.get("charges", 10)
        date = data.get("date", "")
        status = data.get("status", "pending")
        mentor = User.objects.get(username=data["username"])
        picture = data.get("picture", "")
        
        workshop = Workshop.objects.create(title=title,
                            description=description,
                            about=about,
                            charges=charges,
                            date=date,
                            mentor=mentor,
                            picture=picture,
                            status=status,)
        
        workshop = workshop.save()
        return workshop, True