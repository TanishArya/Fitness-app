from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Workout, Nutrition
from .forms import WorkoutForm, NutritionForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render

def home(request):
    return render(request, 'fitness/home.html')  # Create a home.html template

@login_required
def workout_list(request):
    workouts = Workout.objects.filter(user=request.user)
    return render(request, 'fitness/workout_list.html', {'workouts': workouts})

@login_required
def nutrition_list(request):
    nutrition_entries = Nutrition.objects.filter(user=request.user)
    return render(request, 'fitness/nutrition_list.html', {'nutrition_entries': nutrition_entries})

@login_required
def add_workout(request):
    if request.method == 'POST':
        form = WorkoutForm(request.POST)
        if form.is_valid():
            workout = form.save(commit=False)
            workout.user = request.user
            workout.save()
            return redirect('workout_list')
    else:
        form = WorkoutForm()
    return render(request, 'fitness/add_workout.html', {'form': form})

@login_required
def add_nutrition(request):
    if request.method == 'POST':
        form = NutritionForm(request.POST)
        if form.is_valid():
            nutrition = form.save(commit=False)
            nutrition.user = request.user
            nutrition.save()
            return redirect('nutrition_list')
    else:
        form = NutritionForm()
    return render(request, 'fitness/add_nutrition.html', {'form': form})