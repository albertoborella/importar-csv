from django.contrib import admin
from import_export import resources
from .models import Propiedad
from import_export.admin import ImportExportModelAdmin


# Register your models here.

class PropiedadResource(resources.ModelResource):
    class Meta:
        model = Propiedad
        fields = ('id','fecha','latitud','longitud','url','tipo_propiedad','precio','moneda','m2','ambientes')

class PropiedadAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_classes = [PropiedadResource]
    list_display = ['tipo_propiedad','url','precio','moneda','m2','ambientes']
    search_fields = ['tipo_propiedad','precio','moneda','m2','ambientes']
    list_filter = ['ambientes']


admin.site.register(Propiedad, PropiedadAdmin)
admin.site.site_header = '07-MARKETING'
admin.site.site_title = 'BD'
admin.site.index_title = 'Mis Bases de Datos'
admin.site.site_url = None