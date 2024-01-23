from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('home/usuarios/', include('usuario.urls')),
    path('home/pagina_inicial/', views.pagina_inicial_view, name='pagina_inicial'),
    path('formulario/abrir/<int:codigo>', views.abrir_formulario_view, name='abrir_formulario'),
    path('home/fichas_preliminares/', views.fichas_preliminares, name='fichas_preliminares'),
    path('home/fichas_pendentes/', views.fichas_pendentes, name='fichas_pendentes'),
    path('home/fichas_concluidas/', views.fichas_concluidas, name='fichas_concluidas'),
    path('home/fichas/visualizar_ficha/<int:cod_ficha>/<int:cod_formulario>', views.visualizar_ficha_view, name='visualizar_ficha'),
    path('home/fichas/registrar_ficha_notificacao', views.registrar_ficha_notificacao, name='registrar_ficha_notificacao'),
    path('home/fichas/observacoes/<int:cod_ficha>', views.observacoes_view, name='observacoes'),
    path('home/fichas/observacoes/registrar_observacao/', views.registrar_observacao, name='registrar_observacao'),
    path('home/fichas/observacoes/fechar_obervacao/<int:cod_ficha>/<int:cod_obs>', views.fechar_observacao, name='fechar_observacao'),
    # path('home/fichas/observacoes/apagar_obervacao/<int:codigo>', views.apagar_observacao, name='apagar_observacao'),
    path('imagem/<int:cod_img>', views.imagem_local, name='imagem'),
]
