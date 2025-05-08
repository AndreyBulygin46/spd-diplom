from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post, Comment, Like


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ['id', 'username']


class CommentSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['author', 'comment', 'created_at']


class PostSerializer(serializers.ModelSerializer):

    author = UserSerializer(read_only=True)
    comments = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'text', 'image', 'created_at', 'comments', 'likes_count']

    def get_comments(self, obj):
        queryset = obj.comments.all()
        serializer = CommentSerializer(queryset, many=True)
        return serializer.data

    def get_likes_count(self, obj):
        return obj.likes.count()


class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Like
        fields = ['user']
