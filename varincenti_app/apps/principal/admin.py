from django.contrib.auth.models import *
from django.contrib import admin
from .models import *

admin.site.register(Permission)
admin.site.register(Contact)