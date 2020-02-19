from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Compensation

def home(request):
	return render(request, 'analysis/home.html')


def about(request):
	return render(request, 'analysis/about.html')


def search(request):
	qs = Compensation.objects.all()

	industry_param_query = request.GET.get('industry_param')
	nulls_param_query = request.GET.get('nulls_param')
	keywords_param_query = request.GET.get('keywords_param')

	if keywords_param_query != '' and keywords_param_query is not None:
		qs = qs.filter(Orgname__icontains = keywords_param_query)

	context = {
		'queryset': qs
	}

	return render(request, 'analysis/search.html', context)


# Create your views here.
