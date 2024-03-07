# views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# from django.contrib import messages
from account.models import Profile
from account.serializers import UserSerializer, ProfileSerializer
from base.emails import send_account_activation_email
from django.shortcuts import get_object_or_404

class UserViewSet(viewsets.ViewSet):
    def create(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            send_account_activation_email(user.email)
            return Response({"message": "An email has been sent on your mail."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def login(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, username=email, password=password)
        if user and user.profile.is_email_verified:
            login(request, user)
            return Response({"message": "Logged in successfully."}, status=status.HTTP_200_OK)
        return Response({"error": "Invalid credentials or email not verified."}, status=status.HTTP_400_BAD_REQUEST)

    def activate_email(self, request, email_token=None, *args, **kwargs):
        try:
            profile = Profile.objects.get(email_token=email_token)
            profile.is_email_verified = True
            profile.save()
            return Response({"message": "Email verified successfully."}, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response({"error": "Invalid Email token"}, status=status.HTTP_400_BAD_REQUEST)

@login.requred
class ProfileViewSet(viewsets.ViewSet):
    
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request):
        queryset = self.get_queryset()
        serializer = ProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        profile = get_object_or_404(queryset, pk=pk)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        profile = get_object_or_404(self.get_queryset(), pk=pk)
        serializer = ProfileSerializer(profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        profile = get_object_or_404(self.get_queryset(), pk=pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
