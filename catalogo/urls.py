from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('producto/<int:id>/', views.detalles, name='detalles'),
    path('buscar/', views.busqueda_resultado, name='busqueda_resultado'),
    path('productos_por_categoria/<int:id>/', views.productos_por_categoria, name='productos_por_categoria'),
]
