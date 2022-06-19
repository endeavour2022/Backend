import os
import time
from datetime import datetime
from rest_framework.views import APIView
from backend.models import User
from rest_framework.response import Response

import sib_api_v3_sdk
from dotenv import load_dotenv
from sib_api_v3_sdk.rest import ApiException

API_KEY = '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'

    
class SendMail(APIView):
    """
    This class handles send in blue emails 
    """
    
    configuration = sib_api_v3_sdk.Configuration()
    configuration.api_key['api-key'] = API_KEY
    
    @classmethod
    def send_mail_to_agent(cls, data):
        """
        This function used to send email to agent
        """
        
        api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(cls.configuration))
        to = [{"email": data["email"], "name": data["user"].title()}]
        params = {"user":data["user"].title(),"code": data["code"], "templateId": 1}
        
        send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(to=to, params=params, template_id=1)

        try:
            api_response = api_instance.send_transac_email(send_smtp_email)
            return api_response
        except ApiException as e:
            print(e)
            return None
        
    def post(self, request):
        code = request.data.get("code", "")
        username = request.data.get("username", "")
        if User.objects.filter(username=username).exists():
            user = User.objects.get(username=username)
            if user.verification_code == code:
                user.is_active = True
                user.is_verified = True
                user.verification_code = None
                user.save()
                return Response({"message": "Your Account has been verfied, please login to continue"})
            return Response({"error": "Invalid code"})
        return Response({"error": "username does not exist"})
