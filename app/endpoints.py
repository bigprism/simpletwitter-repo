from django.urls import path

from .views import get_posts, create_post, like_post, comment_on_post

urlpatterns = [
    path('posts/', get_posts, name='get_posts'),
    path('create_post/', create_post, name='create_post'),
    path('like_post/<int:pk>/', like_post, name='like_post'),
    path('comment_on_post/<int:pk>/', comment_on_post, name='comment_on_post'),
]