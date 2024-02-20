from django.contrib import admin
from .models import Category, Recipe, Ingredient, Instruction


# class RecipeAdmin(admin.ModelAdmin):
#     list_display = ('title', 'description', 'cooking_time', 'photo', 'category')
#     readonly_fields = ('category',)
#     list_filter = ('category',)



admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Ingredient)
admin.site.register(Instruction)
