from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name = 'main'),
    path('bejegyzesek/', views.bejegyzesek, name = 'bejegyzesek'),
    path('bejegyzesek/<int:osztaly_id>/', views.bejegyzesekOsztalyId, name = 'bejegyzesek-osztaly_id'),
]