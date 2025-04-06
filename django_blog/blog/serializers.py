
from rest_framework import serializers
from .models import Post, Category
from django.contrib.auth.models import User

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']

class PostSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)
    category = CategorySerializer(read_only=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'category', 'created_at', 'updated_at']
