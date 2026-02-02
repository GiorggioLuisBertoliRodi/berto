from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    imagen = CloudinaryField("imagen", blank=True, null=True)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(max_length=100, db_column='Nombre')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.TextField(blank=True, null=True)
    imagen = CloudinaryField("imagen", blank=True, null=True)
    precio = models.DecimalField(max_digits=10, decimal_places=0)

    def __str__(self):
        return self.nombre
class Comentario_Producto(models.Model):
    producto = models.ForeignKey(Producto,related_name='comentarios',on_delete=models.CASCADE)
    autor = models.ForeignKey(User,on_delete=models.CASCADE)
    mensaje = models.TextField(max_length=500)  # más flexible que CharField
    creado = models.DateTimeField(auto_now_add=True)  # fecha automática

    def __str__(self):
        return f'Comentario de {self.autor.username} en {self.producto.nombre}'