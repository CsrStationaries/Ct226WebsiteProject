from django.contrib import admin
from .models import Stationaries

class StationariesAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity')

admin.site.register(Stationaries, StationariesAdmin)