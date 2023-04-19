from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.db.models import Q

from .forms import BejegyzesForm
from .models import Bejegyzes, Tevekenyseg, OSZTALY_CHOICES

def bejegyzesek(request):
    # Form:
    form = BejegyzesForm(request.POST or None)
    if(request.method == "POST"):
        if(form.is_valid()):
            form.save()
            form = BejegyzesForm()
    else:
        form = BejegyzesForm()

    bejegyzesek = Bejegyzes.objects.all()
    tevekenysegek = Tevekenyseg.objects.all()
    osztalyok = OSZTALY_CHOICES

    context = {
        'form': form,
        'bejegyzesek': bejegyzesek,
        'tevekenysegek': tevekenysegek,
        'osztalyok': osztalyok
    }

    return render(request, "app/bejegyzesek.html", context = context)

def bejegyzesekOsztalyId(request, osztaly_id):
    osztaly = None
    for key, value in OSZTALY_CHOICES:
        if(int(key) == osztaly_id - 1):
            osztaly = value

    bejegyzesek = None

    context = {
        'osztaly': osztaly,
        'bejegyzesek': bejegyzesek
    }

    return render(request, "app/osztaly_bejegyzesek.html", context = context)

def bejegyzesFeltoltes(request):
    return HttpResponse("bejegyzés feltöltése")