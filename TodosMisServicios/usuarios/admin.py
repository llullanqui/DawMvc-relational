from django.contrib import admin

from .models import Usuario
from .models import Servicio
from .models import Usuario_Servicio

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Servicio)
admin.site.register(Usuario_Servicio)
