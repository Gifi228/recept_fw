from django.shortcuts import get_object_or_404
from django.shortcuts import render
from .models import Category, Recipe

def main_page(request):
    recipes = Recipe.objects.all()
    context = {
        "title": "Главная страница",
        "recipes": recipes
    }
    return render(request, 'recept/main_page.html', context)

def category_page(request, category_id):
    category = Category.objects.get(pk=category_id)
    recipes = Recipe.objects.filter(category=category)
    context = {
        "title": "Страница категории",
        "category": category,
        "recipes": recipes
    }
    return render(request, 'recept/category_page.html', context )

def recipe_detail(request, recipe_id):
    recipe = Recipe.objects.get(pk=recipe_id)
    context = {
        "title": "Страница рецепта",
        "recipe": recipe
    }
    return render(request, 'recept/recipe_detail.html', context)





def category_page_view(request, category_id):
    recipes = Recipe.objects.filter(category=category_id)

    trends = Recipe.objects.all().order_by('cooking_time')
    category = Category.objects.get(id=category_id)

    context = {
        "title": f"Категория: {category.name}",
        "recipes": recipes,
        "trends": trends
    }

    return render(request, 'recept/category_page.html', context)




def recipe_detail_view(request, recipe_id):
    recipe = get_object_or_404(Recipe, pk=recipe_id)

    context = {
        "title": "Рецепты",
        "recipe": recipe,
    }

    return render(request, "recept/recipe_detail.html", context)