from django.http import HttpResponse
from django.shortcuts import render,redirect,get_object_or_404
from .models import Recipe
from .forms import recipeForm
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
# Create your views here.

def recipe_list(request):
  recipes= Recipe.objects.all()
  return render(request,'recipe_list.html',{'recipes':recipes})
@login_required
def recipe_create(request):
  if request.method=='POST':
    form=recipeForm(request.POST,request.FILES)
    if form.is_valid():
      form.save() 
      return redirect('recipe_list')
    else:
       print(form.errors)
       return render(request, 'recipe_form.html', {'form': form})

  else:
    form=recipeForm()
    return render(request,'recipe_form.html',{'form':form})
def recipe_update(request,recipe_id):
  recipe= get_object_or_404(Recipe, id=recipe_id)
  if request.method=='POST':
    form=recipeForm(request.POST,request.FILES,instance=recipe,)
    if form.is_valid():
      form.save()
      return redirect('recipe_list')
  else:
    form= recipeForm(instance=recipe)
    return render(request,'recipe_form.html',{'form':form})
  
def recipe_delete(request,recipe_id):
  recipe= get_object_or_404(Recipe, id=recipe_id)
  if request.method=='POST':
    recipe.delete()
    return redirect('recipe_list')
  return render(request,'recipe_delete.html', {'recipe':recipe})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            
            next_url = request.GET.get('next') or request.POST.get('next')
            return redirect(next_url if next_url else 'recipe_list')
        else:
            error_message = "Invalid username or password"
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')