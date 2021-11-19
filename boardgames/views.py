from django.shortcuts import render

# Create your views here.

def index(request):
    """The home page for Board Game Website"""
    return render(request, 'boardgames/index.html')