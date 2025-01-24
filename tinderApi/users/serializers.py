from rest_framework import serializers  
from .models import CustomUser  

class CustomUserSerializer(serializers.ModelSerializer):  
    class Meta:  
        model = CustomUser  
        fields = ['id', 'email', 'first_name', 'last_name', 'is_active', 'is_staff'] 

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()