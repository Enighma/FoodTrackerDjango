from django.shortcuts import render
from .models import Food, Meal
from .forms import MealForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

# Create your views here.
def index(request):
	template = "list.html"
	meal = Meal.objects.all()

	context ={
		'meals':meal,
		'title':"Food List"
	}

	return render(request,template,context)

def add_meal(request):
	template = "add_meal.html"


	if request.method == "POST":
		form = MealForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('food:food-index'))
	else:
		context = {
			'meal_form':MealForm(),
			'title':'Add Meal'
		}

	return render(request,template,context)

def delete_meal(request, id):
	meal = Meal.objects.get(id=int(id))
	meal.delete()
	return HttpResponseRedirect(reverse_lazy('food:food-index'))

def update_meal(request, id):
	template = "add_meal.html"

	meal = Meal.objects.get(id=int(id))

	if request.method == "POST":
		form = MealForm(request.POST, instance=meal)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse_lazy('food:food-index'))
	else:
		context = {
			'meal_form':MealForm(instance=meal),
			'title':'Update Meal'
		}

	return render(request,template,context)


def view_meal(request, id):
	template = "view_meal.html"
	meal = Meal.objects.get(id=int(id))

	context = {
		'meal':meal,
		'title':'View Meal'
	}

	return render(request,template,context)

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect(reverse_lazy('food:food-index'))
	else:
		return HttpResponseRedirect(reverse_lazy('auth_login'))


	
