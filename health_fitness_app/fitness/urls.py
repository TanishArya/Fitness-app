from django.urls import path
from . import views

urlpatterns = [
    path('workouts/', views.workout_list, name='workout_list'),
    path('nutrition/', views.nutrition_list, name='nutrition_list'),
    path('add_workout/', views.add_workout, name='add_workout'),
    path('add_nutrition/', views.add_nutrition, name='add_nutrition'),
]