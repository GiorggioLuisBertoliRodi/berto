import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from catalogo.models import Producto, Categoria

# Migrar productos
for p in Producto.objects.all():
    if p.Imagen and not str(p.Imagen).startswith("http"):
        p.Imagen = p.Imagen  # fuerza la subida a Cloudinary
        p.save()
        print(f"Producto {p.Nombre} migrado a Cloudinary")

# Migrar categorías
for c in Categoria.objects.all():
    if c.Imagen and not str(c.Imagen).startswith("http"):
        c.Imagen = c.Imagen
        c.save()
        print(f"Categoría {c.Nombre} migrada a Cloudinary")
