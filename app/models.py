from django.db import models

STATUS_CHOICES = (
    ("0", "Jóvahagyásra vár"),
    ("1", "jovahagyott")
)

OSZTALY_CHOICES = (
    ("0", "SZF1A"),
    ("1", "SZF1B"),
    ("2", "SZF2"),
    ("3", "nSZF1A"),
    ("4", "nSZF1B")
)

# Create your models here.
class Tevekenyseg(models.Models):
    tevekenyseg_id = models.AutoField(primary_key = True, editable = False)
    tevekenyseg_nev = models.CharField(max_length = 50, verbose_name = "Tevékenység neve")
    pontszam = models.IntegerField(verbose_name = "Pontszám")

class Bejegyzes(models.Model):
    tevekenyseg_id = models.ForeignKey(Tevekenyseg, verbose_name ="Tevékenység", on_delete = models.CASCADE)
    osztaly_id = models.CharField(max_length = 10, choices = OSZTALY_CHOICES, verbose_name ="Osztályok")
    allapot = models.CharField(max_length = 50, choices = STATUS_CHOICES, verbose_name ="Állapot")

class User(models.Model):
    name = models.CharField(max_length = 50, verbose_name = 'Név:')
    password = models.CharField(max_length = 50, verbose_name = 'Jelszó')
    email = models.EmailField(max_field = 100, verbose_name = 'E-mail cím')
    osztaly_id = models.CharField(max_length = 10, choices = OSZTALY_CHOICES, verbose_name = "Osztály")