
from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    
    path('<slug:slug>/results/', views.ResultsView.as_view(), name='results'), 
    path('<slug:slug>/vote/', views.vote, name='vote'),
    path('<slug:slug>/', views.DetailView.as_view(), name='detail'),
    path('', views.IndexView.as_view(), name='index')
]