from django.contrib import admin
from .models import Place, PlaceOfInterest, TypePlace


class PlaceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'QR', 'coverage_display', 'location_map',)

    def location_map(self, obj):
        url = 'http://maps.google.com?q=%s' % (obj.location)
        return '<a href="%s" target="_blank" >%s</a>' % (url, obj.location)
    location_map.allow_tags = True

    def coverage_display(self, obj):
        return '%d m' % (obj.coverage)
    coverage_display.short_description = "Coverage"

    location_map.allow_tags = True
    def QR(self, obj):
        return '<a href="%s" target="_blank" ><img src="%s"></a>' % (obj.qr_code, obj.qr_code)
    QR.allow_tags = True

admin.site.register(Place, PlaceAdmin)
admin.site.register(PlaceOfInterest)
admin.site.register(TypePlace)
