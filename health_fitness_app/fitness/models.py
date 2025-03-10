from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User

class Workout(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    exercise = models.CharField(max_length=100)
    duration = models.IntegerField()  # Duration in minutes
    calories_burned = models.IntegerField()

    def __str__(self):
        return f"{self.exercise} on {self.date}"

class Nutrition(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    food_item = models.CharField(max_length=100)
    calories = models.IntegerField()

    def __str__(self):
        return f"{self.food_item} on {self.date}"