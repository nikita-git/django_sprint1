from django.urls import path, URLResolver

from .views import index, post_detail, category_posts

app_name = 'blog'

urlpatterns: list[URLResolver] = [
    path('category/<slug:category_slug>/',
         category_posts,
         name='category_posts'),
    path('posts/<int:post_id>/', post_detail, name='post_detail'),
    path('', index, name='index'),
]
