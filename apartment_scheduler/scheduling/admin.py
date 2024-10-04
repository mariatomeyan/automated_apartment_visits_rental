from django.contrib import admin
from .models import Zone, Runner, Apartment, PotentialTenant, Visit

admin.site.register(Zone)
admin.site.register(Runner)
admin.site.register(Apartment)
admin.site.register(PotentialTenant)
admin.site.register(Visit)
