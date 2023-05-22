from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

class RegisterSerializers (serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True)
    
    class Meta:
        
        model = User
        fields = ('email', 'username', 'password')
        
    def create (self, validated_data):
        
        return User.objects.create_user(**validated_data)
    
class LoginSerializers (serializers.ModelSerializer):
    
    password = serializers.CharField(write_only = True)
    
    class Meta:
        
        model = User
        fields = ('email', 'password', 'token')
        
        #read_only_fields = ['token']