from django.shortcuts import render

# Создаем здесь представления. 
from rest_framework import generics  
from .models import CustomUser  
from .serializers import CustomUserSerializer  
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate

class UserCreateView(generics.CreateAPIView):  
    queryset = CustomUser.objects.all()  
    serializer_class = CustomUserSerializer  

class UserLoginView(generics.GenericAPIView):
     @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'access': openapi.Schema(type=openapi.TYPE_STRING),
                    'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                }
            ),
            400: "Invalid credentials",
        }
    )
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)
        
        if user.check_password(password):
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token
            access_token['email'] = user.email
            return Response({
                'access': str(access_token),
                'refresh': str(refresh)
            }, status=status.HTTP_200_OK)
        
        return Response({"error": "Invalid credentials"}, status=status.HTTP_400_BAD_REQUEST)

   