from django.shortcuts import render, redirect

from .models import Game
from .forms import GameForm

# Create your views here.

def index(request):
    """The home page for Board Game Website"""
    return render(request, 'boardgames/index.html')

def games(request):
    """The page for All Board Games"""
    games = Game.objects.order_by('-date_added')
    context = { 'games': games }
    return render(request, 'boardgames/games.html', context)

def new_game(request):
    """Add a new game."""
    if request.method != 'POST':
        # No data submittes; create a blank form.
        form = GameForm()
    else:
        # POST data submitted; process data.
        form = GameForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boardgames:games')

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'boardgames/new_game.html', context)
