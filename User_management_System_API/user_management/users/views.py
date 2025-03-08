from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer,LoginSerializer,UserProfileSerializer,PasswordChangeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth import update_session_auth_hash


class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registered successfully!"},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                "token": token.key,
                "username": user.username
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProfileView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        try:
            serializer = UserProfileSerializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except AuthenticationFailed:
            return Response(
                {"error": "Invalid token. Please log in again."},
                status=status.HTTP_401_UNAUTHORIZED
            )
            
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            # Delete the token
            request.user.auth_token.delete()
            return Response(
                {"message": "Logout successful."}, 
                status=status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {"error": "Something went wrong. Please try again."},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class PasswordChangeView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            # Check if the old password is correct
            if not request.user.check_password(serializer.validated_data['old_password']):
                return Response(
                    {"old_password": "Incorrect old password."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Set the new password
            request.user.set_password(serializer.validated_data['new_password'])
            request.user.save()

            # Update the session to prevent logout after password change
            update_session_auth_hash(request, request.user)

            return Response(
                {"message": "Password changed successfully."}, 
                status=status.HTTP_200_OK
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)