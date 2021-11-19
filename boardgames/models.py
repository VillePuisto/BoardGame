from django.db import models

# Create your models here.
class Game(models.Model):
    """The Board Game"""
    text = models.CharField(max_length=250)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The string representation of the model"""
        return self.text