from django.urls import path
from . import views


app_name = 'tweet'


urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_tweet, name='create'),
]