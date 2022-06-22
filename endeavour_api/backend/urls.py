from django.contrib import admin
from django.urls import path, include
from backend.views import RegisterUser, LoginUser, UpdateUser, SendMail, CreateIdea, CreateWorkshop, GetAllIdeas, GetAllWorkshops
from . import views

urlpatterns = [
    path('signup/', RegisterUser.as_view(), name="signup"),
    path('login/', LoginUser.as_view(), name="login"),
    path('update/', UpdateUser.as_view(), name="update"),
    path('verify-email/', SendMail.as_view(), name='verify-email'),
    path('create-idea/', CreateIdea.as_view(), name="create-idea"),
    path('create-workshop/', CreateWorkshop.as_view(), name="create-workshop"),
    path('get-ideas/', GetAllIdeas.as_view(), name="get-ideas"),
    path('get-workshops/', GetAllWorkshops.as_view(), name="get-workshops"),
]