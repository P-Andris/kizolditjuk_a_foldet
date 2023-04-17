from django.shortcuts import render
from django.http import HttpResponse

def bejegyzesek(request):
    return HttpResponse("bejegyzések")

def bejegyzesekOsztalyId(request, osztaly_id):
    return HttpResponse(f"{osztaly_id} bejegyzései")

def bejegyzesFeltoltes(request):
    return HttpResponse("bejegyzés feltöltése")