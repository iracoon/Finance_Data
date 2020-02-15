from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request, 'analysis/home.html')


def about(request):
	return render(request, 'analysis/about.html')


def search(request):
	return render(request, 'analysis/search.html')


# Create your views here.
