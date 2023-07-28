from django.db import models

# Create your models here.
class Propiedad(models.Model):
    fecha = models.CharField(max_length=20, blank=True, null=True)
    latitud = models.CharField(max_length=100, blank=True, null=True)
    longitud = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField()
    tipo_propiedad = models.CharField(max_length=100, blank=True, null=True)
    precio = models.CharField(max_length=100, blank=True, null=True)
    moneda = models.CharField(max_length=100, blank=True, null=True)
    m2 = models.CharField(max_length=100, blank=True, null=True)
    ambientes = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name = 'Propiedad'
        verbose_name_plural = 'Propiedades'
        ordering = ['id']

    def __str__(self):
        return self.tipo_propiedad
