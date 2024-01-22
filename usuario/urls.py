from . import views
from django.urls import path


urlpatterns = [
    path('', views.usuarios_view, name='usuarios'),
    path('logar_usuario/', views.logar_usuario, name='logar_usuario'),
]