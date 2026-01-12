from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Categoria(models.Model):
    Nombre = models.CharField(max_length=100)
    Imagen = CloudinaryField("Imagen", blank=True, null=True)

    def __str__(self):
        return self.Nombre

class Producto(models.Model):
    Nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Descripcion = models.TextField(blank=True,null=True)
    Imagen = CloudinaryField("Imagen", blank=True, null=True)
    Precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.Nombre
