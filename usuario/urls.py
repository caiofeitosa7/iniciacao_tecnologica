from . import views
from django.urls import path


urlpatterns = [
    path('', views.listar_usuarios, name='usuarios'),
    # path('listar/', views.listar_usuarios, name='usuarios'),
]