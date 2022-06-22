import json
import random
from rest_framework import status

from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import Workshop
from backend.serializers import WorkshopSerializer

class GetAllWorkshops(APIView):
    
    def get(self, request):
        
        authenticated = request.data.get("isAuthenticated", False)
        
        if not authenticated:
            return Response({"alert": "youre not allowed to open this page"})
        all_workshops = Workshop.objects.filter(status='active')

        import pdb
        pdb.set_trace()    
        result = WorkshopSerializer(all_workshops, many=True)
        return Response({"result": result.data}, status=status.HTTP_200_OK)