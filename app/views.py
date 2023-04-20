from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Q, Sum, Count

from .forms import BejegyzesForm
from .models import Bejegyzes, Tevekenyseg, OSZTALY_CHOICES

def main(request):
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

    osszpontszamok = Bejegyzes.objects.values('osztaly_id').annotate(osszpontszam = Sum('tevekenyseg_id_id__pontszam')).filter(Q(allapot__exact = 'Jóváhagyott')).order_by('-osszpontszam')

    context = {
        'form': form,
        'bejegyzesek': bejegyzesek,
        'tevekenysegek': tevekenysegek,
        'osztalyok': osztalyok,
        'osszpontszamok': osszpontszamok
    }

    return render(request, "app/index.html", context = context)

def bejegyzesek(request):
    bejegyzesek = Bejegyzes.objects.all()
    osztalyok = OSZTALY_CHOICES

    context = {
        'bejegyzesek': bejegyzesek,
        'osztalyok' : osztalyok
    }

    return render(request, "app/bejegyzesek.html", context = context)

def bejegyzesekOsztalyId(request, osztaly_id):
    osztaly = None
    for key, value in OSZTALY_CHOICES:
        if(int(key) == osztaly_id - 1):
            osztaly = value

    bejegyzesek = Bejegyzes.objects.filter(Q(osztaly_id__exact = osztaly_id))

    context = {
        'osztaly': osztaly,
        'bejegyzesek': bejegyzesek
    }

    return render(request, "app/osztaly_bejegyzesek.html", context = context)