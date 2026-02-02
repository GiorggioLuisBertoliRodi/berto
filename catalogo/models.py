from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User


class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100
        # ❌ Quitar db_column="Nombre"
    )
    imagen = CloudinaryField(
        "imagen",
        blank=True,
        null=True
        # opcional: solo usar db_column si la columna real en DB no coincide
    )

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    nombre = models.CharField(
        max_length=100,
        db_column="Nombre"
    )

    # ForeignKey usa por defecto categoria_id (CONFIRMADO por el error)
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
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
        on_delete=models.CASCADE
    )

    autor = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    mensaje = models.TextField(
        max_length=500
    )

    creado = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Comentario de {self.autor.username} en {self.producto.nombre}"
