import json
import os

from rest_framework.response import Response
from backend.models import Idea, User
from rest_framework.views import APIView
from rest_framework import status
class ApprovePost(APIView):
    
    def post(self, request):
        
        post = request.data.get("post", None)
        username = request.data.get("username", None)
        try:
            idea = Idea.objects.get(id=post)
            approver = User.objects.get(username=username)
        except:
            return Response({"error": "data not found"})
        idea.status = "active"
        idea.approved_by = f"{approver.first_name} {approver.last_name}"
        
        idea.save()
        
        return Response({"message": "approved"})
        
        