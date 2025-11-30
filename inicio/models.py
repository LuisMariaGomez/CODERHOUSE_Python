from django.db import models
class Arco(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    potencia = models.IntegerField()
    precio = models.FloatField()
    tipo = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='imagenes_arcos', null=True, blank=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.potencia}) - {self.tipo} (${self.precio})"