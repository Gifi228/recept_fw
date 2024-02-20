# recipes_app/models.py
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    cooking_time = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='recipe_photos/', blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)


class Instruction(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
