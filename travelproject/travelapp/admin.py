from django.contrib import admin
#from django.db import models
# Register your models here.
from . models import Place
from . models import Place1

admin.site.register(Place)
admin.site.register(Place1)