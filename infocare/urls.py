from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('home/usuarios/', include('usuario.urls')),
    path('home/pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    path('imagem/<int:cod_img>', views.imagem_local, name='imagem'),
    path('ficha/', views.abrir_ficha, name='abrir_ficha'),
    path('ficha/set_ficha_notificacao', views.set_ficha_notificacao, name='set_ficha_notificacao')
]
