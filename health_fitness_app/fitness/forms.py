from django import forms
from .models import Workout, Nutrition

class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['date', 'exercise', 'duration', 'calories_burned']  # Removed leading space

class NutritionForm(forms.ModelForm):
    class Meta:
        model = Nutrition
        fields = ['date', 'food_item', 'calories']