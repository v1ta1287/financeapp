from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
import logging

# Create your views here.

def index(request):
	return render(request, 'index.html')

def display_all(request):
	items =  Expense.objects.all()
	context = {
		'items': items,
		'header': 'All Expenses'
	}
	return render(request, 'expenses.html', context)

def display_important(request):
	items =  Expense.objects.all().filter(importance__gte = 5)
	context = {
		'items': items,
		'header': 'Important Expenses'
	}
	return render(request, 'expenses.html', context)

def add_expense(request):
	if request.method == "POST":
		form = ExpenseForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('display1')
	else: 
		form = ExpenseForm()
		return render(request, 'add_new.html', {'form': form})

def edit_expense(request, pk):
	item = get_object_or_404(Task, pk = pk)

	if request.method =="POST":
		form = ExpenseForm(request.POST, instance = item)
		if form.is_valid():
			form.save()
			return redirect('display1')

	else:
		form = ExpenseForm(instance = item)
		return render(request, 'edit.html', {'form': form})

def delete_expense(request,pk):
	Expense.objects.filter(id=pk).delete()
	items = Expense.objects.all()

	context = {
		'items': items
	}
	return render(request, 'expenses.html')