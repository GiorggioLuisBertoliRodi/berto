from django.contrib import admin
from .models import Categoria, Producto,Comentario_Producto

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ("nombre", "imagen")

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio", "imagen")
    search_fields = ("nombre",)
admin.site.register(Comentario_Producto)
class ComentarioProductoAdmin(admin.ModelAdmin):
    list_display = ("usuario", "producto", "comentario", "fecha")
    search_fields = ("comentario", "usuario__username")
    list_filter = ("producto", "fecha")