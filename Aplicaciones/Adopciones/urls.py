from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.index, name='index'),
    path('nueva_persona/', views.nueva_persona, name='nueva_persona'),
    path('listar_persona/', views.listar_persona, name='listar_persona'),
    path('editar_persona/<int:id_per>/', views.editar_persona, name='editar_persona'),
    path('eliminar_persona/<int:id_per>/', views.eliminar_persona, name='eliminar_persona'),


     path('nueva_mascota/', views.nueva_mascota, name='nueva_mascota'),
    path('listar_mascota/', views.listar_mascota, name='listar_mascota'),
    path('editar_mascota/<int:id>/', views.editar_mascota, name='editar_mascota'),
    path('eliminar_mascota/<int:id>/', views.eliminar_mascota, name='eliminar_mascota'),


    path('nueva_adopcion/', views.nueva_adopcion, name='nueva_adopcion'),
    path('listar_adopcion/', views.listar_adopcion, name='listar_adopcion'),
    path('editar_adopcion/<int:id>/', views.editar_adopcion, name='editar_adopcion'),
    path('eliminar_adopcion/<int:id>/', views.eliminar_adopcion, name='eliminar_adopcion'),
]
