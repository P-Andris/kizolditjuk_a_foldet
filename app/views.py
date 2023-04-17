from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def tevekenyseg(request):
    tevekenyseg_id = get_object_or_404(Tevekenyseg, pk = id)
    return HttpResponse("tevekenyseg")

def bejegyzesek(request):
        return HttpResponse("bejegyzesek")

def bejegyzesekFeltoltes(request):
        return HttpResponse("bejegyzesek Feltoltese")