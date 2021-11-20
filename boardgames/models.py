from django.db import models

# Create your models here.
class Game(models.Model):
    """The Board Game"""
    text = models.CharField(max_length=250)
    #makeshift owner field, self entered. Need user accounts to have auto tracked
    owner = models.JSONField(default="mystery")
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The string representation of the model"""
        return self.text

class GameInfo(models.Model):
    #Info about a board game, loaning clicked by owner
    #Gamekey = models.ForeignKey(Game)
    description = models.TextField(default="describe your game")
    onLoan = models.BooleanField(default=False)
    date_modified = models.DateTimeField(auto_now_add=True)

    #delete description when game is deleted
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    
    def __str__(self):
        #return the first bit of the description
        return self.text[:50] + "..."