from . import views
from django.urls import path


urlpatterns = [
    path('', views.usuarios_view, name='usuarios'),
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('cadastrar_usuario/', views.cadastrar_usuario_view, name='cadastrar_usuario'),
    path('visualizar_usuario/<int:codigo>', views.visualizar_usuario_view, name='visualizar_usuario'),
    path('logout/', views.logout, name='logout')
]