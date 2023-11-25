from django.db import models
from django.contrib.auth.models import User

# Create your models here.
from django.db import models

# game room 
class GameRoom(models.Model):
    name = models.CharField(max_length=100)
    # Other fields like creator, players, current_round, etc.

# for drawing
class Drawing(models.Model):
    room = models.ForeignKey(GameRoom, on_delete=models.CASCADE)
    drawer = models.ForeignKey(User, on_delete=models.CASCADE)
    word_to_draw = models.CharField(max_length=50)
    # Other fields like drawing_data, timestamp, etc.

# For guessing purposes
class Guess(models.Model):
    drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    guessed_word = models.CharField(max_length=50)
    # Other fields like is_correct, timestamp, etc.


'''

# game/models.py

from django.db import models
from django.contrib.auth.models import User

# game session 
class GameSession(models.Model):
    name = models.CharField(max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)  # info about user who created the session
    start_time = models.TimeField()
    end_time = models.TimeField()
    game_status = 

# player 
class Player(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    # You might have additional player-related fields like drawing history, guessing history, etc.

# drawing
class Drawing(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    drawing_data = models.TextField()
    # Other fields like timestamp, round_number, etc., can be added as necessary.

# guess mechnanism
class Guess(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game_session = models.ForeignKey(GameSession, on_delete=models.CASCADE)
    guessed_word = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)
    # Additional fields for timestamp, round_number, etc., as per the game requirements.


'''