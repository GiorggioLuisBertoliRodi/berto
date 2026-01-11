from django.db import models

# Create your models here.

class Categoria(models.Model):
    Nombre = models.CharField(max_length=100)
    Imagen = models.ImageField(upload_to='categorias/')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    Nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    Descripcion = models.TextField()
    Imagen = models.ImageField(upload_to='productos/')
    Precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.nombre
