from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_list_or_404
from .models import Profile,Post
from .serializers import PostSerializer,ProfileSerializer
from rest_framework import generics

class ProfileDetails(generics.ListCreateAPIView):
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    
class PostDetails(generics.ListCreateAPIView):
    queryset=Post.objects.all()
    serializer_class=PostSerializer
   
