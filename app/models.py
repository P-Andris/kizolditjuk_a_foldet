from django.db import models
from django.contrib.auth.models import AbstractUser

# STATUS_CHOICES = (
#     ("0", "Jóvahagyásra vár"),
#     ("1", "jovahagyott")
# )

OSZTALY_CHOICES = (
    ("0", "SZF1A"),
    ("1", "SZF1B"),
    ("2", "SZF2"),
    ("3", "nSZF1A"),
    ("4", "nSZF1B")
)

STATUS_CHOICES = (
    ("Jóvahagyásra vár", "Jóvahagyásra vár"),
    ("Jóváhagyott", "Jóváhagyott")
)

# OSZTALY_CHOICES = (
#     ("SZF1A", "SZF1A"),
#     ("SZF1B", "SZF1B"),
#     ("SZF2", "SZF2"),
#     ("nSZF1A", "nSZF1A"),
#     ("nSZF1B", "nSZF1B")
# )

# Create your models here.
class Tevekenyseg(models.Model):
    tevekenyseg_id = models.AutoField(primary_key = True, editable = False)
    tevekenyseg_nev = models.CharField(max_length = 100, unique = True, verbose_name = "Tevékenység neve")
    pontszam = models.IntegerField(verbose_name = "Pontszám")

    def __str__(self):
        return self.tevekenyseg_nev

class Bejegyzes(models.Model):
    tevekenyseg_id = models.ForeignKey(Tevekenyseg, on_delete = models.CASCADE, verbose_name = "Tevékenység")
    osztaly_id = models.CharField(max_length = 10, choices = OSZTALY_CHOICES, verbose_name = "Osztály")
    allapot = models.CharField(max_length = 50, choices = STATUS_CHOICES, default = "Jóvahagyásra vár", verbose_name = "Állapot")

    def __str__(self):
        return f"{self.tevekenyseg_id} | {self.osztaly_id} | {self.allapot}"

class User(AbstractUser):
    username = models.CharField(max_length = 50, unique = True, verbose_name = 'Username')
    password = models.CharField(max_length = 50, verbose_name = 'Password')
    email = models.EmailField(max_length = 100, unique = True, verbose_name = 'E-mail')
    osztaly_id = models.CharField(max_length = 10, choices = OSZTALY_CHOICES, verbose_name = "Osztály")

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'email', 'osztaly_id']

    def __str__(self):
        return self.username