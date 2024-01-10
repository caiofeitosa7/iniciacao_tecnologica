from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('home/usuarios/', include('usuario.urls')),
    path('home/pagina_inicial/', views.pagina_inicial, name='pagina_inicial'),
    path('home/fichas_preliminares/', views.fichas_preliminares, name='fichas_preliminares'),
    path('home/fichas_pendentes/', views.fichas_pendentes, name='fichas_pendentes'),
    path('home/fichas_concluidas/', views.fichas_concluidas, name='fichas_concluidas'),
    path('imagem/<int:cod_img>', views.imagem_local, name='imagem'),
    path('ficha/<int:codigo>', views.abrir_ficha, name='abrir_ficha'),
    path('ficha/set_ficha_notificacao', views.set_ficha_notificacao, name='set_ficha_notificacao')
]
