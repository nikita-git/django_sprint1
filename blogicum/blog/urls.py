from django.urls import path

from .views import index, post_detail, category_post

app_name = 'blog'

urlpatterns = [
    path('category/<slug:category_slug>/', category_post, name='category_post'),
    path('posts/<int:id>/', post_detail, name='post_detail'),
    path('', index, name='index'),
]
