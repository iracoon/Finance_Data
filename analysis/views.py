from django.shortcuts import render
from bson.json_util import dumps
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, UserPassesTestMixin
from django.db import connection
from django.template import RequestContext
from django.db.models import Q
from django.views.generic import (
	ListView, 
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)
from .models import Compensation
from .models import Honoraria
from .models import Post
from django.core.paginator import Paginator

def home(request):
	return render(request, 'analysis/home.html')

def about(request):
	return render(request, 'analysis/about.html')

class FindListView(ListView):
	model = Compensation
	context_object_name = 'compensations'
	template_name = 'analysis/find/find.html'

#general info page
def stats(request):
	# cursor = connection.cursor()
	# cursor.execute('SELECT * FROM analysis_honoraria')
	persons = Honoraria.objects.raw('SELECT * FROM analysis_honoraria') # fetchall() may not be the right call here?
	return render(request, 'analysis/stats.html', {'persons':persons})


def graphs(request):
	return render(request, 'analysis/graphs.html')


class ResearchListView(ListView):
	model = Post
	template_name = 'analysis/research.html'
	context_object_name = 'posts'
	ordering = ['-date_posted']


class ResearchDetailView(DetailView):
	model = Post
	template_name = 'analysis/research_detail.html'


class ResearchDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	template_name = 'analysis/research_confirm_delete.html'
	success_url = '/research/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False


class ResearchCreateView(LoginRequiredMixin, CreateView):
	model = Post
	template_name = 'analysis/research_form.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)


class ResearchUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	template_name = 'analysis/research_form.html'
	fields = ['title', 'content']

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

#Search Page

class SearchCompensationDetailView(DetailView):
	model = Compensation
	template_name = 'analysis/search/search_detail.html'

class SearchCompensationListView(ListView):
	model = Compensation
	context_object_name = 'compensations'
	template_name = 'analysis/search/search-analysis-compensation.html'

	def get_queryset(self):
		industry_param_query = self.request.GET.get('industry_param')
		nulls_param_query = self.request.GET.get('nulls_param')
		keywords_param_query = self.request.GET.get('keywords_param')

		qs = Compensation.objects.all()

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
			qs = qs.exclude(Realcode__isnull=True).exclude(Realcode__exact='')
		
		paginator = Paginator(qs, 10)

		page = self.request.GET.get('page')
		qs = paginator.get_page(page)

		return qs;

class SearchHonorariaListView(ListView):
	model = Honoraria
	context_object_name = 'honorarias'
	template_name = 'analysis/search/search-analysis-honoraria.html'

	def get_queryset(self):
		industry_param_query = self.request.GET.get('industry_param')
		nulls_param_query = self.request.GET.get('nulls_param')
		keywords_param_query = self.request.GET.get('keywords_param')

		qs = Honoraria.objects.all()

		return qs;
