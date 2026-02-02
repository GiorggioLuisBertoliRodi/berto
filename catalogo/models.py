from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100,
        db_column="Nombre"
    )
    imagen = CloudinaryField(
        "imagen",
        blank=True,
        null=True,
        db_column="Imagen"
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(
        max_length=100,
        db_column="Nombre"
    )

    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        db_column="Categoria_id"
    )

    descripcion = models.TextField(
        blank=True,
        null=True,
        db_column="Descripcion"
    )

    imagen = CloudinaryField(
        "imagen",
        blank=True,
        null=True,
        db_column="Imagen"
    )

    precio = models.DecimalField(
        max_digits=10,
        decimal_places=0,
        db_column="Precio"
    )

    def __str__(self):
        return self.nombre


class Comentario_Producto(models.Model):
    producto = models.ForeignKey(
        Producto,
        related_name="comentarios",
        on_delete=models.CASCADE,
        db_column="Producto_id"
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="Autor_id"
    )

    mensaje = models.TextField(
        max_length=500,
        db_column="Mensaje"
    )

    creado = models.DateTimeField(
        auto_now_add=True,
        db_column="Creado"
    )

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.producto.nombre}"
