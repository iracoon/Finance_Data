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

	# keywords search for all columns in table
	if keywords_param_query != '' and keywords_param_query is not None:
		qs = qs.filter(Q(ID__icontains = keywords_param_query)
			| Q(Chamber__icontains = keywords_param_query)
			| Q(CID__icontains = keywords_param_query)
			| Q(CalendarYear__icontains = keywords_param_query)
			| Q(ReportType__icontains = keywords_param_query)
			| Q(CompSource__icontains = keywords_param_query)
			| Q(Orgname__icontains = keywords_param_query)
			| Q(Ultorg__icontains = keywords_param_query)
			| Q(Realcode__icontains = keywords_param_query)
			| Q(Source__icontains = keywords_param_query)
			| Q(CompSourceLocation__icontains = keywords_param_query)
			| Q(CompDuties__icontains = keywords_param_query)
			| Q(dupe__icontains = keywords_param_query))

	# specify by industry, or select all industries
	if industry_param_query != '' and industry_param_query is not None:
		qs = qs.filter(Realcode=industry_param_query)

	# include nulls in industry column
	if nulls_param_query == 'on':
		print("IM CALLED")
		qs = qs.exclude(Realcode__isnull=True).exclude(Realcode__exact='')

	#test commit

	context = {
		'queryset': qs
	}

	return render(request, 'analysis/search.html', context)


# Create your views here.
