from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Post, Like, Comment
from .serializers import PostSerializer, LikeSerializer, CommentSerializer
# Create your views here.


class CreatePostView(generics.CreateAPIView):
    """Этот класс позволяет создавать новые посты."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class ListPostView(generics.ListAPIView):
    """Этот класс позволяет просматривать список всех постов."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class RetrievePostView(generics.RetrieveAPIView):
    """Этот класс позволяет просматривать отдельный пост по его идентификатору."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UpdatePostView(generics.UpdateAPIView):
    """Этот класс позволяет редактировать существующий пост по его идентификатору."""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            return Response({"Ошибка": "Вы не можете редактировать чужой пост"}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

class DeletePostView(generics.DestroyAPIView):
    """Этот класс позволяет удалять существующий пост по его идентификатору."""
    permission_classes = [permissions.IsAuthenticated]
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            return Response({"Ошибка": "Можно удалять только свои посты"}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()

class CreateCommentView(generics.CreateAPIView):
    """Этот класс позволяет создавать новые комментарии к постам."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = Post.objects.get(pk=post_id)
        serializer.save(author=self.request.user, post=post)

class ListCommentView(generics.ListAPIView):
    """Этот класс позволяет просматривать список всех комментариев к посту по его идентификатору."""
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)
    serializer_class = CommentSerializer

class RetrieveCommentView(generics.RetrieveAPIView):
    """Этот класс позволяет просматривать отдельный комментарий по его идентификатору."""
    def get_object(self):
        comment_id = self.kwargs['comment_id']
        return Comment.objects.get(pk=comment_id)
    serializer_class = CommentSerializer

class UpdateCommentView(generics.UpdateAPIView):
    """Этот класс позволяет редактировать существующий комментарий по его идентификатору."""
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)
    serializer_class = CommentSerializer

    def perform_update(self, serializer):
        if self.request.user != serializer.instance.author:
            return Response({"Ошибка": "Можно менять только свои комментарии"}, status=status.HTTP_403_FORBIDDEN)
        serializer.save()

class DeleteCommentView(generics.DestroyAPIView):
    """Этот класс позволяет удалять существующий комментарий по его идентификатору."""
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comment.objects.filter(post_id=post_id)

    def perform_destroy(self, instance):
        if self.request.user != instance.author:
            return Response({"Ошибка": "Можно удалять только свои комментарии"}, status=status.HTTP_403_FORBIDDEN)
        instance.delete()

class CreateLikeView(generics.CreateAPIView):
    """Этот класс позволяет создавать новые лайки к постам."""
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        post_id = self.request.data.get('post')
        post = Post.objects.get(pk=post_id)
        user = self.request.user

        if Like.objects.filter(post=post, user=user).exists():
            return Response({"Ошибка": "Вы уже оценили этот пост"}, status=status.HTTP_400_BAD_REQUEST)

        serializer.save(post=post, user=user)

class ListLikeView(generics.ListAPIView):
    """Этот класс позволяет просматривать список всех лайков к посту по его идентификатору."""
    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Like.objects.filter(post_id=post_id)
    serializer_class = LikeSerializer