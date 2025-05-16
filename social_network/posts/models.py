from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):

    text = models.TextField(blank=False)                  # текст поста
    author = models.ForeignKey(User,
                             on_delete=models.CASCADE)    # автор поста
    image = models.ImageField(upload_to='posts/images/',
                             blank=True)                  # изображение поста
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания поста
    likes_count = models.IntegerField(default=0)          # кол-во лайков поста

    def __str__(self):
        return self.text


# для доп. задания
# class PostImage(models.Model):
#     ...


class Like(models.Model):

    post = models.ForeignKey(Post,
                             related_name='likes',
                             on_delete=models.CASCADE) # пост, на который поставлен лайк
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE) # автор лайка

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'Like by {self.user} on {self.post}'




class Comment(models.Model):

    post = models.ForeignKey(Post,
                             related_name='comments',
                             on_delete=models.CASCADE)    # пост, на который оставлен коммент
    author = models.ForeignKey(User,
                               on_delete=models.CASCADE)  # автор комментария
    comment = models.TextField(blank=False)               # текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # дата создания комментария


    def __str__(self):
        return self.comment