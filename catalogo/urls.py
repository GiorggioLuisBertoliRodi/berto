from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('detalles/<int:id>/', views.detalles, name='detalles'),
    path('buscar/', views.busqueda_resultado, name='busqueda_resultado'),
    path('productos_por_categoria/<int:id>/', views.productos_por_categoria, name='productos_por_categoria'),
    path('ver_comentarios/<int:id>/',views.ver_comentarios,name='ver_comentarios'),
    path('comentar/<int:id>/',views.comentar,name='comentar')
]
