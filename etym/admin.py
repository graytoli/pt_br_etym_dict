from django.contrib import admin
from django_google_maps import widgets as map_widgets
from django_google_maps import fields as map_fields

from .models import Modern, Origin, Language, Region

admin.site.register(Modern)
admin.site.register(Origin)
admin.site.register(Language)

class RegionAdmin(admin.ModelAdmin):
    formfield_overrides = {
        map_fields.AddressField: {'widget': map_widgets.GoogleMapsAddressWidget},
    }
admin.site.register(Region, RegionAdmin)
