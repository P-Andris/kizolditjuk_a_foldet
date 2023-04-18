from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import BejegyzesForm
from .models import Bejegyzes, Tevekenyseg

def bejegyzesek(request):
    # Form:
    form = BejegyzesForm(request.POST or None)
    if(request.method == "POST"):
        if(form.is_valid()):
            form.save()
    else:
        form = BejegyzesForm()

    # Table:
    bejegyzesek = Bejegyzes.objects.all()

    context = {
        'form': form,
        'bejegyzesek': bejegyzesek
    }

    return render(request, "app/bejegyzesek.html", context = context)

def bejegyzesekOsztalyId(request, osztaly_id):
    return HttpResponse(f"{osztaly_id} bejegyzései")

def bejegyzesFeltoltes(request):
    return HttpResponse("bejegyzés feltöltése")