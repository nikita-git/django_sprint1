from django.urls import path

from .views import rules, about

app_name = 'pages'

urlpatterns = [
    path('rules/', rules, name='rules'),
    path('about/', about, name='about'),
]
