from django.urls import path, URLResolver

from .views import rules, about

app_name = 'pages'

urlpatterns: list[URLResolver] = [
    path('rules/', rules, name='rules'),
    path('about/', about, name='about'),
]
