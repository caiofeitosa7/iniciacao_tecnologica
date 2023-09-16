from . import views
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('home/pagina_inicial/', views.pagina_inicial),
    path('home/usuarios/', include('usuario.urls'))
]
