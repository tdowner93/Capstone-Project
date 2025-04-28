from django.db import models
from django.contrib.auth.models import User

class GolfCourse(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Weather(models.Model):
    temperature = models.FloatField()
    wind_speed = models.FloatField()
    wind_direction = models.CharField(max_length=5)
    is_raining = models.BooleanField()
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Weather data for {self.city} at {self.timestamp}"
    
class ScoreEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hole_number = models.IntegerField()
    strokes = models.IntegerField()
    putts = models.IntegerField()
    green_in_regulation = models.BooleanField(default=False)
    fairways_hit = models.BooleanField(default=False)
    up_and_down = models.BooleanField(default=False)

    def __str__(self):
        return f"User: {self.user.username}, Hole: {self.hole_number}"
