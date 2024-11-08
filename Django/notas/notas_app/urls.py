from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_notas, name='lista_notas'),
    path('crear/', views.crear_nota, name='crear_nota'),
    path('editar/<int:pk>/', views.editar_nota, name='editar_nota'),
    path('eliminar/<int:pk>/', views.eliminar_nota, name='eliminar_nota'),
]
