from django.shortcuts import render,get_object_or_404,redirect
from django.conf import settings
import random
from .models import *
from .forms import ComentarioForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    productos_list = list(Producto.objects.all())
    Productos_home = random.sample(productos_list, min(len(productos_list), 5))
    categorias = Categoria.objects.all()
    return render(request, 'catalogo/home.html', {"Productos_home": Productos_home,"categorias": categorias})
from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Producto


def busqueda_resultado(request):
    # Texto de búsqueda
    query = request.GET.get('q', '').strip()

    # Query base (ordenado para evitar warnings de paginación)
    productos_qs = Producto.objects.all().order_by('id')

    # Filtro por nombre (búsqueda)
    if query:
        productos_qs = productos_qs.filter(nombre__icontains=query)

    # Paginación
    paginator = Paginator(productos_qs, 5)  # 5 productos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(
        request,
        'catalogo/busqueda_resultado.html',
        {
            'productos': page_obj.object_list,
            'page_obj': page_obj,
            'query': query,
        }
    )

def detalles(request, id):
    producto_detalles = get_object_or_404(Producto, id=id)
    return render(request, 'catalogo/Detalles.html', {'producto_detalles': producto_detalles})

def productos_por_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    productos = Producto.objects.filter(categoria=categoria)
    categorias = Categoria.objects.all()

    return render(request, 'catalogo/productos_por_categoria.html', {
        'Productos_home': productos,
        'categorias': categorias,
        'categoria_actual': categoria
    })
def ver_comentarios(request,id):
    producto = get_object_or_404(Producto,id=id)
    comentarios = producto.comentarios.all()
    return render(request,'catalogo/ver_comentarios.html',{"producto":producto,"comentarios":comentarios})

@login_required
def comentar(request,id):
    producto = get_object_or_404(Producto,id=id)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            Comentario_Producto.objects.create(
                autor=request.user,
                producto=producto,
                mensaje=form.cleaned_data['mensaje']
            )

            return redirect('ver_comentarios',id=producto.id)
    else:
        form = ComentarioForm
    return render(request,'catalogo/comentar.html',{"form":form,"producto":producto})