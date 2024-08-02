from django.db import models
from django.urls import reverse

class Lista(models.Model):  # Asegúrate de usar la mayúscula inicial
    nombre1 = models.CharField(max_length=100)
    nombre2 = models.CharField(max_length=100)
    fecha_ingreso = models.DateField(null=True, blank=True)
    fecha_egreso = models.DateField('Salida', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('nombre-detalle', args=[str(self.id)])

    def __str__(self):
        return f'{self.nombre2}, {self.nombre1}'
