from django.db import models
from pkg_resources import require



SEXO_CHOICES = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
]


class ESP32(models.Model):
    serial = models.CharField(max_length=64)
    ip = models.GenericIPAddressField()
    puerto = models.IntegerField()


class Entrada(models.Model):
    esp32 = models.ForeignKey(ESP32, on_delete=models.PROTECT)
    valor = models.FloatField()
    fechaHora = models.DateTimeField()
    procesado = models.BooleanField()


class Salida(models.Model):
    esp32 = models.ForeignKey(ESP32, on_delete=models.PROTECT)
    valor = models.FloatField()
    fechaHora = models.DateTimeField()
    procesado = models.BooleanField()


class Cliente(models.Model):
    esp32 = models.ForeignKey(ESP32, on_delete=models.PROTECT)
    nombre = models.CharField(max_length=64)
    apellido = models.CharField(max_length=64)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=64)
    foto = models.ImageField(null=True, blank=True)

