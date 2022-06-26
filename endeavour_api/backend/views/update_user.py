import json
from rest_framework.response import Response
from rest_framework.views import APIView
from django_email_verification import send_email
from backend.models import User
from backend.serializers import UserSerializer
from rest_framework import generics, permissions, status, views

class UpdateUser(APIView):
    def post(self, request, *args, **kwargs):
        user, is_valid = self.update(data=request.data)
        if is_valid:
            return Response({"message": user})
        return Response({"message": user})
    
    def update(self, data):
        
        username = data.get("username", "")
        password = data.get("password", "")
        is_authenticated = data.get("isAuthenticated", False)
        
        if not is_authenticated:
            return ({"error": "You dont have access to perform this task"}), False
        
        if not username:
            return ({"error": "Please enter a user name"}), False
        
        if not password:
            return ({"error": "Please enter password"}), False
        
        
        if User.objects.filter(username=username, password=password).exists():
            user = User.objects.get(username=username, password=password)
        
            first_name = data.get("first_name", user.first_name)
            last_name = data.get("last_name", user.last_name)
            phone = data.get("phone", user.phone)
            linkedin_link = data.get("linkedin_link", user.linkedin_link)
            bio = data.get("bio", user.bio)
            designation = data.get("designation", user.designation)
            city = data.get("city", user.city)
            projects = data.get("projects", user.projects)
            new_password = data.get("new_password", "")
               
            user.first_name=first_name,
            user.last_name=last_name,
            user.phone=phone,
            user.linkedin_link=linkedin_link,
            user.bio=bio,
            user.designation=designation,
            user.city=city,
            user.projects=projects,
            if new_password:
                user.password=new_password
            user = user.save()
        
            return ({"success": "profile updated"}), True
        
        return ({"error": "user does not exist"}), False