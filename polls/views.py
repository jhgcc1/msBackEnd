from django.contrib.auth.models import User
from rest_framework import generics
from polls.serializers import UsersSerializer, PostSerializer, PostSerializerWithUser
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from polls.models import Posts
from rest_framework.permissions import IsAuthenticated

        
class UserCreate(generics.CreateAPIView):
    serializer_class = UsersSerializer
    permission_classes = (AllowAny, )

class createPostNew(generics.ListCreateAPIView):
    authentication_classes = [authentication.TokenAuthentication]
    def get_queryset(self):
        user = self.request.user
        return Posts.objects.all()

    def get_serializer_class(self):
        if self.request.method =='GET':
            return PostSerializerWithUser
        if self.request.method =='POST':
            return PostSerializer





