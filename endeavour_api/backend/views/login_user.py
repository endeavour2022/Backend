from asyncio import FastChildWatcher
from numpy import true_divide
from backend.models import User
import json
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.serializers import UserSerializer

class LoginUser(APIView):
    def post(self, request):
        username = request.data.get("username", None)
        email = request.data.get("email",  None)
        password = request.data.get("password", None)
        
        if username and password:
            if User.objects.filter(username=username, password=password).exists():
                user = User.objects.get(username=username, password=password)
                if not user.is_active == False:
                    user = UserSerializer(user)
                    return Response({"user": user.data, "authenticated": True})
                return Response({"alert": "Your Account is not verified, please verify your mail", "authenticated": False})
            return Response({"alert": "Provide valid username and password", "authenticated": True})
        
        elif email and password:
            if User.objects.filter(email=email, password=password).exists():
                user = User.objects.get(email=email, password=password)
                if not user.is_active == False:
                    user = UserSerializer(user)
                    return Response({"user": user.data, "authenticated": True})
                return Response({"alert": "Your Account is not verified, please verify your mail", "authenticated": False})
            return Response({"alert": "Provide valid email and password", "authenticated": True})
        else:
            return Response({"alert": "Provide valid username and password", "authenticated": False})        
   