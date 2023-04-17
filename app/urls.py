from django.urls import path
from . import views

urlpatterns = [
    path('tevekenysegek/', views.tevekenyseg, name = 'tevekenysegek'),
    path('bejegyzesek/', views.bejegyzesek, name = 'bejegyzesek'),
    path('bejegyzesekFeltoltes/', views.bejegyzesekFeltoltes, name = 'bejegyzesek_feltoltes')
]