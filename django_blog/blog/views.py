from django.shortcuts import render
from .models import BlogPost

def home(request):
    posts = BlogPost.objects.all()
    return render(request, 'blog/home.html', {'posts': posts})
# Create your views here.

from rest_framework import generics
from .models import Post, Category
from .serializers import PostSerializer, CategorySerializer

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer

class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
