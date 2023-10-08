from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('home/pagina_inicial/', views.pagina_inicial),
    path('home/usuarios/', include('usuario.urls')),
    path('imagem/<int:cod_img>', views.imagem_local, name='imagem'),
]
