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
from .models import Post

from .models import Compensation ####
from .models import Agreement
from .models import Asset ####
from .models import Gift
from .models import Income
from .models import Liability
from .models import Position
from .models import Transaction
from .models import Travel
from .models import Honoraria #####
from .models import Indivs
from .models import PACs

from .models import Bills ####
from .models import Votes ###
from .models import Cosponsor ###

from .models import MemberInfo

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
	template_name = 'analysis/search/search_compensation_detail.html'

class SearchHonorariaDetailView(DetailView):
	model = Honoraria
	template_name = 'analysis/search/search_detail.html'

class SearchAssetDetailView(DetailView):
	model = Asset
	template_name = 'analysis/search/search_detail.html'

class SearchCompensationListView(ListView):
	model = Compensation
	context_object_name = 'compensations'
	template_name = 'analysis/search/search-analysis-compensation.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = Compensation.objects.all()

		# keywords search for all columns in table
		if keyword != '' and keyword is not None:
			qs = qs.filter(Q(ID__icontains = keyword)
				| Q(Chamber__icontains = keyword)
				| Q(CID__icontains = keyword)
				| Q(CalendarYear__icontains = keyword)
				| Q(ReportType__icontains = keyword)
				| Q(CompSource__icontains = keyword)
				| Q(Orgname__icontains = keyword)
				| Q(Ultorg__icontains = keyword)
				| Q(Realcode__icontains = keyword)
				| Q(Source__icontains = keyword)
				| Q(CompSourceLocation__icontains = keyword)
				| Q(CompDuties__icontains = keyword)
				| Q(dupe__icontains = keyword))

		# specify by industry, or select all industries
		if ind != 'All...' and keyword is not None:
			qs = qs.filter(Realcode=ind)

		# specify by congress person, or select all congresspeople
		if person != 'All...' and person is not None:
			qs = qs.filter(CID=person.split("__",1)[1])

		paginator = Paginator(qs, 10)

		page = self.request.GET.get('page')
		qs = paginator.get_page(page)

		return qs;

class SearchHonorariaListView(ListView):
	model = Honoraria
	context_object_name = 'honorarias'
	template_name = 'analysis/search/search-analysis-honoraria.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = Honoraria.objects.all()

		# keywords search for all columns in table
		if keyword != '' and keyword is not None:
			qs = qs.filter(Q(ID__icontains = keyword)
				| Q(Chamber__icontains = keyword)
				| Q(CID__icontains = keyword)
				| Q(CalendarYear__icontains = keyword)
				| Q(ReportType__icontains = keyword)
				| Q(HonorariaSource__icontains = keyword)
				| Q(Orgname__icontains = keyword)
				| Q(Ultorg__icontains = keyword)
				| Q(Realcode__icontains = keyword)
				| Q(Source__icontains = keyword)
				| Q(HonorariaSourceLoc__icontains = keyword)
				| Q(HonorariaActivity__icontains = keyword)
				| Q(HonorariaDate__icontains = keyword)
				| Q(HonorariaDateText__icontains = keyword)
				| Q(HonorariaAmt__icontains = keyword)
				| Q(HonorariaAmtText__icontains = keyword)
				| Q(Dupe__icontains = keyword))

		# specify by industry, or select all industries
		if ind != 'All...' and keyword is not None:
			qs = qs.filter(Realcode=ind)

		# specify by congress person, or select all congresspeople
		if person != 'All...' and person is not None:
			qs = qs.filter(CID=person.split("__",1)[1])

		paginator = Paginator(qs, 10)

		page = self.request.GET.get('page')
		qs = paginator.get_page(page)

		return qs;

class SearchAssetListView(ListView):
	model = Asset
	context_object_name = 'assets'
	template_name = 'analysis/search/search-analysis-asset.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = Asset.objects.all()

		# keywords search for all columns in table
		if keyword != '' and keyword is not None:
			qs = qs.filter(Q(ID__icontains = keyword)
				| Q(Chamber__icontains = keyword)
				| Q(CID__icontains = keyword)
				| Q(CalendarYear__icontains = keyword)
				| Q(SenAB__icontains = keyword)
				| Q(AssetSpouseJointDep__icontains = keyword)
				| Q(AssetSource__icontains = keyword)
				| Q(Orgname__icontains = keyword)
				| Q(Realcode__icontains = keyword)
				| Q(Source__icontains = keyword)
				| Q(AssetDescrip__icontains = keyword)
				| Q(Orgname2__icontains = keyword)
				| Q(Ultorg2__icontains = keyword))

		# specify by industry, or select all industries
		if ind != 'All...' and keyword is not None:
			qs = qs.filter(Realcode=ind)

		# specify by congress person, or select all congresspeople
		if person != 'All...' and person is not None:
			qs = qs.filter(CID=person.split("__",1)[1])

		paginator = Paginator(qs, 10)

		page = self.request.GET.get('page')
		qs = paginator.get_page(page)

		return qs;

class SearchBillsListView(ListView):
	model = Bills
	context_object_name = 'bills'
	template_name = 'analysis/search/search-analysis-bills.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = Bills.objects.all()

		# # keywords search for all columns in table
		# if keyword != '' and keyword is not None:
		# 	qs = qs.filter(Q(ID__icontains = keyword)
		# 		| Q(Chamber__icontains = keyword)
		# 		| Q(CID__icontains = keyword)
		# 		| Q(CalendarYear__icontains = keyword)
		# 		| Q(SenAB__icontains = keyword)
		# 		| Q(AssetSpouseJointDep__icontains = keyword)
		# 		| Q(AssetSource__icontains = keyword)
		# 		| Q(Orgname__icontains = keyword)
		# 		| Q(Realcode__icontains = keyword)
		# 		| Q(Source__icontains = keyword)
		# 		| Q(AssetDescrip__icontains = keyword)
		# 		| Q(Orgname2__icontains = keyword)
		# 		| Q(Ultorg2__icontains = keyword))

		# # specify by industry, or select all industries
		if ind != 'All...' and keyword is not None:
			qs = qs.filter(policy_area=ind)

		# specify by congress person, or select all congresspeople
		if person != 'All...' and person is not None:
			qs = qs.filter(sponsor_id=person.split('__')[0])

		paginator = Paginator(qs, 10)

		page = self.request.GET.get('page')
		qs = paginator.get_page(page)

		return qs;

class SearchCosponsorListView(ListView):
	model = Cosponsor
	context_object_name = 'cosponsors'
	template_name = 'analysis/search/search-analysis-cosponsor.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = Cosponsor.objects.all()

		# specify by congress person, or select all congresspeople
		if person != 'All...' and person is not None:
			qs = qs.filter(Cosponsor=person.split('__')[0])

		paginator = Paginator(qs, 10)

		page = self.request.GET.get('page')
		qs = paginator.get_page(page)

		return qs;


class SearchVotesListView(ListView):
	model = Cosponsor
	context_object_name = 'votes'
	template_name = 'analysis/search/search-analysis-votes.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = Votes.objects.all()

		paginator = Paginator(qs, 10)

		page = self.request.GET.get('page')
		qs = paginator.get_page(page)

		return qs;

class SearchIndivsListView(ListView):
	model = Indivs
	context_object_name = 'indivs'
	template_name = 'analysis/search/search-analysis-indivs.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = Indivs.objects.all()


		# specify by industry, or select all industries
		if ind != 'All...' and keyword is not None:
			qs = qs.filter(Realcode=ind)

		# specify by congress person, or select all congresspeople
		if person != 'All...' and person is not None:
			qs = qs.filter(RecipID=person.split("__",1)[1])

		# paginator = Paginator(qs, 10)

		# page = self.request.GET.get('page')
		# qs = paginator.get_page(page)

		return qs;

class SearchPACsListView(ListView):
	model = PACs
	context_object_name = 'pacs'
	template_name = 'analysis/search/search-analysis-pacs.html'

	def get_queryset(self):
		ind = self.request.GET.get('ind')
		person = self.request.GET.get('person')
		keyword = self.request.GET.get('keyword')
		qs = PACs.objects.all()


		# specify by industry, or select all industries
		if ind != 'All...' and keyword is not None:
			qs = qs.filter(Realcode=ind)

		# specify by congress person, or select all congresspeople
		if person != 'All...' and person is not None:
			qs = qs.filter(CID=person.split("__",1)[1])

		# paginator = Paginator(qs, 10)

		# page = self.request.GET.get('page')
		# qs = paginator.get_page(page)

		return qs;