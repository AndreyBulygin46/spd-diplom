"""
URL configuration for social_network project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', views.ListPostView.as_view(), name='list_posts'),
    path('posts/<int:pk>/', views.RetrievePostView.as_view(), name='post_detail'),
    path('posts/<int:pk>/update/', views.UpdatePostView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', views.DeletePostView.as_view(), name='post_delete'),
    path('posts/<int:pk>/create_comment/', views.CreateCommentView.as_view(), name='post_create_comment'),
    path('posts/<int:pk>/comments/', views.ListCommentView.as_view(), name='list_comments'),
    path('posts/<int:pk>/comments/<int:comment_id>/', views.RetrieveCommentView.as_view(), name='retrieve_comment'),
    path('posts/<int:pk>/comments/<int:comment_id>/update/', views.UpdateCommentView.as_view(), name='post_update_comment'),
    path('posts/<int:pk>/comments/<int:comment_id>/delete/', views.DeleteCommentView.as_view(), name='post_delete_comment'),
    path('posts/<int:pk>/likes/', views.CreateLikeView.as_view(), name='post_likes'),
    path('posts/<int:pk>/all_likes/', views.ListLikeView.as_view(), name='post_likes')
]