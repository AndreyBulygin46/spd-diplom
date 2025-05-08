from django.contrib import admin
from .models import Comment, Like, Post, User

# Register your models here.
admin.site.register(Post)
admin.site.register(Like)
admin.site.register(Comment)
