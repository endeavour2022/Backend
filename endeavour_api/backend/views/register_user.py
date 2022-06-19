import json
import random
from rest_framework.response import Response
from rest_framework.views import APIView
from backend.models import User
from backend.serializers import UserSerializer
from .send_mail import SendMail

class RegisterUser(APIView):
    def post(self, request, *args, **kwargs):
        message, is_valid = self.create(data=request.data)
        if is_valid:
            user = UserSerializer(message)
            code = generate_verification_code(request.data["username"])
            data = {
                "user": request.data.get("first_name", "there"),
                "code": code,
                "email": request.data.get("email", "endeavour.ucp@gmail.com"),
            }
            SendMail.send_mail_to_agent(data)
            return Response({"message": "Account created succesfully"})
        return Response({"message": message})
    
    def create(self, data):
        first_name = data.get("first_name", "")
        last_name = data.get("last_name", "")
        username = data.get("username", "")
        phone = data.get("phone", "")
        linkedin_link = data.get("linkedin_link", "")
        photo = data.get("photo", "")
        bio = data.get("bio", "")
        joining_date = data.get("joining_date", "")
        designation = data.get("designation", "")
        city = data.get("city", "")
        email = data.get("email", "")
        projects = data.get("projects", "")
        year_of_experience = data.get("year_of_experience", 0)
        password = data.get("password", "")
        
        if User.objects.filter(username=username).exists():
              return ({"error": "username already exist"}), False
          
        if User.objects.filter(email=email).exists():
              return ({"error": "Email already registered, please try another"}), False
        
        if not username:
            return ({"error": "Please enter a user name"}), False
        
        if not email:
            return ({"error": "Please enter a email"}), False
        
        if not password:
            return ({"error": "Please enter password"}), False
        
        user = User.objects.create(first_name=first_name,
                            last_name=last_name,
                            username=username,
                            phone=phone,
                            linkedin_link=linkedin_link,
                            photo=photo,
                            bio=bio,
                            joining_date=joining_date,
                            designation=designation,
                            city=city,
                            email=email,
                            projects=projects,
                            year_of_experience=year_of_experience,
                            password=password)
        
        user = user.save()
        return user, True
    
def generate_verification_code(username):
    user = User.objects.get(username=username)
    verification_code = random.randint(000000, 999999)
    user.verification_code = verification_code
    user.save()
    
    return verification_code

    

    