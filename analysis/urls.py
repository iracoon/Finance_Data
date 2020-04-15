from django.urls import path
from .views import (
	ResearchListView, 
	ResearchDetailView,
	ResearchCreateView, 
	ResearchUpdateView,
	ResearchDeleteView,
	SearchDetailView, 
	SearchCompensationListView,
	SearchHonorariaListView,
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
	path('search/compensation/',  SearchCompensationListView.as_view(), name='analysis-search-compensation'),
	path('search/honoraria/',  SearchHonorariaListView.as_view(), name='analysis-search-honoraria'),
	path('search/<pk>/', SearchDetailView.as_view(), name='analysis-search-detail'),
	path('find/', FindListView.as_view(), name='analysis-find'),
	path('stats/', views.stats, name='analysis-stats'),
	path('graphs/', views.graphs, name='analysis-graphs'),
]