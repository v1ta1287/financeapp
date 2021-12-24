from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
import logging

# Create your views here.
def login_page(request):
	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		try:
			user = User.objects.get(username = username)
		except: 
			print('hi')
			messages.error(request, 'Username does not exist')

		user = authenticate(request, username = username, password = password)
		if user is not None:
			login(request, user)
			return redirect('index')
		else:
			messages.error(request, 'Username or password is incorrect')

	context = {}
	return render(request, 'login.html', context)

def logout_user(request):
	logout(request)
	return redirect('index')

def index(request):
	return render(request, 'index.html')

@login_required(login_url='login')
def display_all(request):
	items =  Expense.objects.all().filter(user = request.user)
	total = items.aggregate(Sum('amount'))

	context = {
		'items': items,
		'header': 'All Expenses', 
		'total' : total['amount__sum'],

	}
	return render(request, 'expenses.html', context)

def display_important(request):
	items =  Expense.objects.all().filter(importance__gte = 5).filter(user = request.user)
	total = items.aggregate(Sum('amount'))
	context = {
		'items': items,
		'header': 'Important Expenses',
		'total' : total['amount__sum'],
	}
	return render(request, 'expenses.html', context)

def add_expense(request):
	if request.method == "POST":
		form = ExpenseForm(request.POST)

		if form.is_valid():
			expense = form.save(commit=False)
			expense.user = request.user
			expense.save()
			return redirect('display1')
	else: 
		form = ExpenseForm()
		return render(request, 'add_new.html', {'form': form})

def edit_expense(request, pk):
	item = get_object_or_404(Expense, pk = pk)

	if request.method =="POST":
		form = ExpenseForm(request.POST, instance = item)
		if form.is_valid():
			expense = form.save(commit=False)
			expense.user = request.user
			expense.save()
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

def display_statistics(request):
	return render(request, 'stats.html')
	
def display_calculator(request):
	return render(request, 'calculator.html')