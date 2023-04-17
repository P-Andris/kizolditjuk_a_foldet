from django.urls import path
from . import views

urlpatterns = [
    path('bejegyzesek/', views.bejegyzesek, name = 'bejegyzesek'),
    path('bejegyzesek/<int:osztaly_id>/', views.bejegyzesekOsztalyId, name = 'bejegyzesek-osztaly_id'),
    path('bejegyzes/', views.bejegyzesFeltoltes, name = 'bejegyzes')
    # path('tevekenysegek/', views.tevekenyseg, name = 'tevekenysegek'),
    # path('bejegyzesek/', views.bejegyzesek, name = 'bejegyzesek'),
    # path('bejegyzesekFeltoltes/', views.bejegyzesekFeltoltes, name = 'bejegyzesek_feltoltes')
]