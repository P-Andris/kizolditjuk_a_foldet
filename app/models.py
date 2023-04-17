from django.db import models

STATUS_CHOINCES = (
    ("0", "jovahagyasra var"),
    ("1", "jovahagyott")
)

# Create your models here.
class Bejegyzes(models.Model):
    tevekenyseg_id = models.ForeignKey(Tevekenyseg, verbose_name ="tevekenyseg", on_delete = models.CASCADE)
    osztaly_id = models.models.ForeignKey("Osztaly", verbose_name ="osztalyok", on_delete = models.CASCADE)
    allapot = models.models.CharField(max_length = 50,choices = STATUS_CHOINCES ,verbose_name ="allapot")

class Tevekenyseg(models.Models):
    tevekenyseg_id = models.AutoField(primary_key = True, editable = False, verbose_name ="tevekenyseg_id")
    tevekenyseg_nev = models.models.CharField( max_length = 50, verbose_name = "tevekenyseg nev")
    pontszam = models.models.IntegerField(verbose_name = "pontszam")