from django.contrib import admin

from .models import Establishment, AvailabilityEstablishment


class EstablishmentAdmin(admin.ModelAdmin):
    search_fields = ['name']


class AvailabilityEstablishmentAdmin(admin.ModelAdmin):
    search_fields = ['establishment__name']
    list_filter = ['available', 'date']


admin.site.register(Establishment, EstablishmentAdmin)
admin.site.register(AvailabilityEstablishment, AvailabilityEstablishmentAdmin)
