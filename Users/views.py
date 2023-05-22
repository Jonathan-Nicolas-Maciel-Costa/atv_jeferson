from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .serializers import RegisterSerializers,\
                         LoginSerializers
from rest_framework import response, status
from django.contrib.auth import authenticate, login
# Create your views here.

class RegisterAPIView(GenericAPIView):
    
    serializer_class = RegisterSerializers
    
    def post (self, request):
        
        serializers = self.serializer_class(data=request.data)
        
        if serializers.is_valid():
            serializers.save()
            return response.Response(serializers.data, status=status.HTTP_201_CREATED)
        
class LoginAPIView(GenericAPIView):
    
    serializer_class = LoginSerializers
    
    def post (self, request):
        
        email=request.data.get('email', None)
        password = request.data.get('password', None)
        
        user=authenticate(username=email, password=password)
        print(user.token)
        if user:
            
            serializer = self.serializer_class(user)
            
            return response.Response(serializer.data, status=status.HTTP_200_OK)
        
        return response.Response({"Message" : "Invalid Login Informations"}, status=401)