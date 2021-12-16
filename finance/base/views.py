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
	items =  Task.objects.all()
	context = {
		'items': items,
		'header': 'All Tasks'
	}
	return render(request, 'index.html', context)

def display_done(request):
	items =  Task.objects.all().filter(status = "DONE")
	context = {
		'items': items,
		'header': 'Completed Tasks'
	}
	return render(request, 'index.html', context)

def add_task(request):
	if request.method == "POST":
		form = TaskForm(request.POST)

		if form.is_valid():
			form.save()
			return redirect('index')
	else: 
		form = TaskForm()
		return render(request, 'add_new.html', {'form': form})

def edit_task(request, pk):
	item = get_object_or_404(Task, pk = pk)

	if request.method =="POST":
		form = TaskForm(request.POST, instance = item)
		if form.is_valid():
			form.save()
			return redirect('index')

	else:
		form = TaskForm(instance = item)
		return render(request, 'edit.html', {'form': form})

def delete_task(request,pk):
	Task.objects.filter(id=pk).delete()
	items = Task.objects.all()

	context = {
		'items': items
	}
	return render(request, 'index.html')