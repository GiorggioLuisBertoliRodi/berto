from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User

# ==========================
# Categorías de productos
# ==========================
class Categoria(models.Model):
    nombre = models.CharField(
        max_length=100,
        db_column="Nombre"  # coincide con la columna existente en DB
    )
    imagen = CloudinaryField(
        "imagen",
        blank=True,
        null=True,
        db_column="Imagen"  # coincide con la columna existente en DB
    )

    def __str__(self):
        return self.nombre


# ==========================
# Productos
# ==========================
class Producto(models.Model):
    nombre = models.CharField(
        max_length=100,
        db_column="Nombre"  # coincide con la DB
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE
        # no db_column aquí: Django usa categoria_id por defecto
    )
    descripcion = models.TextField(
        blank=True,
        null=True,
        db_column="Descripcion"  # coincide con la DB
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


# ==========================
# Comentarios de productos
# ==========================
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
