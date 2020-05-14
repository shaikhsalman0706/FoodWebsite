from django.shortcuts import render, get_object_or_404
from .models import Food

def homepage(request):
    foods = Food.objects
    return render(request, 'easyfoodshood/home.html', {'foods':foods})

def recipe(request, food_id):
    food_recipe = get_object_or_404(Food, pk=food_id)
    return render(request, 'easyfoodshood/recipe.html', {'food':food_recipe})

