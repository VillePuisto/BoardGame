from django.shortcuts import render
from .models import Game

# Create your views here.

def index(request):
    """The home page for Board Game Website"""
    return render(request, 'boardgames/index.html')

def games(request):
    """The page for All Board Games"""
    games = Game.objects.order_by('date_added')
    context = {'games': games}
    return render(request, 'boardgames/games.html', context)