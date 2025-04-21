from django.db import models

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
