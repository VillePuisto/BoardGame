from django.urls import path
from . import views

app_name= 'boardgames'
urlpatterns= [
    #Home page
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
]