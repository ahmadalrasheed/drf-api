from django.shortcuts import render
from django.views import generic
# from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .models import Post
from .serializer import PostSerializer



# Create your views here.
class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
