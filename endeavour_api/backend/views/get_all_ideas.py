import json
import random
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Idea
from backend.serializers import IdeaSerializer

class GetAllIdeas(APIView):
    
    def get(self, request):
        
        authenticated = request.data.get("isAuthenticated", False)
        type = request.data.get("status", 'active')
        username = request.data.get("username", 'sample')
        
        if not authenticated:
            return Response({"alert": "youre not allowed to open this page"})
        if type == 'active':
            all_ideas = Idea.objects.filter(status='active')
        elif type == 'pending':
            all_ideas = Idea.objects.filter(status='pending', creator__username=username)
        elif type == 'rejected':
            all_ideas = Idea.objects.filter(status='rejected', creator__username=username)

        import pdb
        pdb.set_trace()    
        result = IdeaSerializer(all_ideas, many=True)
        return Response({"result": result.data}, status=status.HTTP_200_OK)
        