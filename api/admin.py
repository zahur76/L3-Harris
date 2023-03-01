from django.contrib import admin

from .models import Airport


class AirportAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
        'icao_code'
    )


# The model followed by class name (model, class name)
admin.site.register(Airport, AirportAdmin)
