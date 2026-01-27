from django.shortcuts import render,get_object_or_404,redirect
from django.conf import settings
import random
from .models import *
from django.core.paginator import Paginator
def home(request):
    productos_list = list(Producto.objects.all())
    Productos_home = random.sample(productos_list, min(len(productos_list), 5))
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/home.html', {"Productos_home": Productos_home,"categorias": categorias})
def busqueda_resultado(request):
    busqueda = request.GET.get('busqueda', '')  
    if busqueda:
        Coincidencias = Producto.objects.filter(nombre__icontains=busqueda)
        Coincidencias = Paginator(Coincidencias,5)
        page_number = request.GET.get('page')
        page_obj = Coincidencias.get_page(page_number)
        return render(request, 'catalogo/busqueda_resultado.html', {'productos': page_obj})
def detalles(request,id):
    producto_detalles = get_object_or_404(Producto,id=id)
    return render(request,'catalogo/Detalles.html',{'producto_detalles':producto_detalles})

def productos_por_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()

    return render(request, 'catalogo/productos_por_categoria.html', {
        'Productos_home': productos,
        'categorias': categorias,
        'categoria_actual': categoria
    })
