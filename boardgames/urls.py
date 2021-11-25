from django.urls import path
from . import views

app_name= 'boardgames'
urlpatterns= [
    #Home page
    path('', views.index, name='index'),
    path('games/', views.games, name='games'),
    #Page for adding a new game
    path('new_game/', views.new_game, name='new_game'),
]