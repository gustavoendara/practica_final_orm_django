from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

current_year = datetime.date.today().year

class Laboratorio(models.Model):
    nombre = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255, null=True)
    pais = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.nombre

class DirectorGeneral(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.OneToOneField(Laboratorio, on_delete=models.CASCADE)
    especialidad = models.CharField(max_length=255, default='Sin especialidad')
    


    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    f_fabricacion = models.IntegerField(
    validators=[MinValueValidator(1900), MaxValueValidator(current_year)],
    help_text="Ingrese solo el año de fabricación."
)
    p_costo = models.DecimalField(max_digits=12, decimal_places=2)
    p_venta = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.nombre


