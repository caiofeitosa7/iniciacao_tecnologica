import os

from django.http import FileResponse
from django.templatetags.static import static
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from . import settings


def login(request):
    imagem_url = imagem_local(request, 0)
    return render(request, 'login.html', {'img_url': imagem_url})


def home(request):
    return render(request, 'base.html')


def pagina_inicial(request):
    return JsonResponse({'html': [render_to_string('pagina_inicial.html')]})


def imagem_local(request, cod_img):
    if not cod_img:
        imagem_url = os.path.join('templates', 'images', 'bg-login.png')

    return FileResponse(open(imagem_url, 'rb'))

























