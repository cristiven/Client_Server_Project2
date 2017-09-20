# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Recolector
from .models import Propietario
from .models import AdminCooperativa
from .models import Superusuario
from .models import SuperNumerario

# Register your models here.

admin.site.register(Recolector)
admin.site.register(Propietario)
admin.site.register(AdminCooperativa)
admin.site.register(Superusuario)
admin.site.register(SuperNumerario)