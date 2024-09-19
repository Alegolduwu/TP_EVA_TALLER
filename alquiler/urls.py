from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_videojuegos,name='listar_videojuegos'),
    path('añadirvideojuego/',views.añadir_videojuego,name= 'añadir_videojuego'),
    path('registraralquiler/',views.registrar_alquiler,name= 'registrar_alquiler'),
    path('añadir_videojuego/',views.añadir_videojuego,name= 'añadir_videojuego'),
    path('generos/',views.list_genero,name='list_generos'),
    path('plataformas/',views.list_plataforma,name='list_plataforma'),
    path('videojuegos_genero/<int:id>',views.videojuegos_genero,name='videojuegos_genero'),
    path('videojuegos_plataforma/<int:id>',views.videojuegos_plataforma,name='videojuegos_plataforma'),
    path('finalizar_alquiler/<int:id>',views.finalizar_alquiler,name='finalizar_alquiler')
]

