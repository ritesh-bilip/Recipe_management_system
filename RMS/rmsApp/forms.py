from django import forms

from .models import Recipe

class recipeForm(forms.ModelForm):
  class Meta:
    model=Recipe
    fields=['name','description','ingredients','instructions','image']