from django.contrib import admin

from letgo.models import imggal
from letgo.models import about
from letgo.models import Contact
from letgo.models import homedesc
from letgo.models import Ourservice



# Register your models here.
admin.site.register(imggal)

admin.site.register(about) 

admin.site.register(Contact)

admin.site.register(homedesc)

admin.site.register(Ourservice)

