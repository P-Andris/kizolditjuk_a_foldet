from django.contrib import admin
from .models import Tevekenyseg, Bejegyzes, User

# Register your models here.
admin.site.register(Tevekenyseg)
admin.site.register(Bejegyzes)
admin.site.register(User)