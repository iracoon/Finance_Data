from django.urls import path
from .views import (
	ResearchListView, 
	ResearchDetailView,
	ResearchCreateView, 
	ResearchUpdateView,
	ResearchDeleteView,
	SearchCompensationDetailView, 
	###########
	SearchCompensationListView,
	# SearchAgreementListView,
	SearchAssetListView,
	# SearchGiftListView,
	# SearchIncomeListView,
	# SearchLiabilityListView,
	# SearchPositionListView,
	# SearchTransactionListView,
	# SearchTravelListView,
	SearchHonorariaListView,
	SearchIndivsListView,
	SearchPACsListView,
	SearchBillsListView,
	SearchCosponsorListView,
	SearchVotesListView,
	##########
	FindListView)
from . import views

urlpatterns = [
	path('', views.home, name='analysis-home'),
	path('about/', views.about, name='analysis-about'),
	path('research/', ResearchListView.as_view(), name='analysis-research'),
	path('research/<int:pk>/', ResearchDetailView.as_view(), name='analysis-research-detail'),
	path('research/new/', ResearchCreateView.as_view(), name='research-create'),
	path('research/<int:pk>/update/', ResearchUpdateView.as_view(), name='analysis-research-update'),
	path('research/<int:pk>/delete/', ResearchDeleteView.as_view(), name='analysis-research-delete'),
	###############
	path('search/compensation/',  SearchCompensationListView.as_view(), name='analysis-search-compensation'),
	# path('search/agreement/',  SearchAgreementListView.as_view(), name='analysis-search-agreement'),
	path('search/asset/',  SearchAssetListView.as_view(), name='analysis-search-asset'),
	# path('search/gift/',  SearchGiftListView.as_view(), name='analysis-search-gift'),
	# path('search/income/',  SearchIncomeListView.as_view(), name='analysis-search-income'),
	# path('search/liability/',  SearchLiabilityListView.as_view(), name='analysis-search-liability'),
	# path('search/position/',  SearchPositionListView.as_view(), name='analysis-search-position'),
	# path('search/transaction/',  SearchTransactionListView.as_view(), name='analysis-search-transaction'),
	# path('search/travel/',  SearchTravelListView.as_view(), name='analysis-search-travel'),
	path('search/honoraria/',  SearchHonorariaListView.as_view(), name='analysis-search-honoraria'),
	path('search/indivs/',  SearchIndivsListView.as_view(), name='analysis-search-indivs'),
	path('search/pacs/',  SearchPACsListView.as_view(), name='analysis-search-PACs'),
	path('search/sponsors/',  SearchBillsListView.as_view(), name='analysis-search-sponsors'),
	path('search/cosponsors/',  SearchCosponsorListView.as_view(), name='analysis-search-cosponsors'),
	path('search/votes/',  SearchVotesListView.as_view(), name='analysis-search-votes'),
	#########
	path('search/compensation/<pk>/', SearchCompensationDetailView.as_view(), name='analysis-search-compensation-detail'),
	path('find/', FindListView.as_view(), name='analysis-find'),
	path('stats/', views.stats, name='analysis-stats'),
	path('graphs/', views.graphs, name='analysis-graphs'),
]