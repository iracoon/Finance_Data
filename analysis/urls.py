from django.urls import path
from .views import (
	ResearchListView, 
	ResearchDetailView,
	ResearchCreateView, 
	SearchDetailView, 
	SearchListView)
from . import views

urlpatterns = [
	path('', views.home, name='analysis-home'),
	path('about/', views.about, name='analysis-about'),
	path('research/', ResearchListView.as_view(), name='analysis-research'),
	path('research/<int:pk>/', ResearchDetailView.as_view(), name='analysis-research-detail'),
	path('research/new/', ResearchCreateView.as_view(), name='analysis-research-create'),
	path('search/',  SearchListView.as_view(), name='analysis-search'),
	path('search/<pk>/', SearchDetailView.as_view(), name='analysis-search-detail')
]