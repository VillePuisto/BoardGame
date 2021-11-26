from django import forms
from django.db.models import fields

from .models import Game, Loan

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['text', 'owner']
        labels = {'text': '', 'owner': ''}

class LoanForm(forms.ModelForm):
    class Meta:
        model=Loan
        fields= ['loaner', 'on_loan']

