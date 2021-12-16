from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib import messages
from .models import Task
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

