from django.db import models


class Game(models.Model):
    """The Board Game"""
    text = models.CharField(max_length=250)
    description = models.TextField(default="Describe your game")
    owner = models.CharField(default="Owner", max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The string representation of the model"""
        return self.text


class Loan(models.Model):
    # Loaning the game, loaner writes their name and ticks a box
    loaner = models.CharField(max_length=50, default="Write your name")
    on_loan = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now_add=True)

    # delete description when game is deleted
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        # return name of the loaner
        return self.loaner[:50]
