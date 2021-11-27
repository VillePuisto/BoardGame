from django.shortcuts import render, redirect

from .models import Game, Loan
from .forms import GameForm, LoanForm

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

def new_loan(request, game_id):
    game=Game.objects.get(id=game_id)
    """Loan a game."""
    if request.method != 'POST':
        # No data submittes; create a blank form.
        form = LoanForm()
    else:
        # POST data submitted; process data.
        form = LoanForm(data=request.POST)
        if form.is_valid():
           new_loan=form.save(commit=False)
           new_loan.game = game
           new_loan.save()
           return redirect('boardgames:game' , game_id=game_id)

    # Display a blank or invalid form.
    context = {'game': game ,'form': form}
    return render(request, 'boardgames/new_loan.html', context)

def game(request, game_id):
    """Show a single game and it's availability"""
    game = Game.objects.get(id=game_id)
    loans = game.loan_set.order_by('loaner')
    context = {'game': game, 'loans': loans}
    return render(request, 'boardgames/game.html', context)

def edit_loan(request, loan_id):
    """Edit an existing loan."""
    loan = Loan.objects.get(id=loan_id)
    game = loan.game

    if request.method != 'POST':
        #Initial request; pre-fill form with the current loan.
        form = LoanForm(instance=loan)
    else:
        #POST data submitted; Process data
        form = LoanForm(instance=loan, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('boardgames:game', game_id=game.id)

    context = {'loan': loan, 'game': game, 'form': form}
    return render(request, 'boardgames/edit_loan.html', context)

def loan_delete(request, loan):
    loan = Loan.objects.get(id=loan)  # Get your current cat

    if request.method == 'POST':         # If method is POST,
        loan.delete()                     # delete the cat.
        return redirect('/games')             # Finally, redirect to the homepage.

    return render(request, 'boardgames/games', {'loan': loan })