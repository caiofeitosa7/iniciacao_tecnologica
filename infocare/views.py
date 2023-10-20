import os

from django.http import FileResponse
from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


def login(request):
    imagem_url = imagem_local(request, 0)
    return render(request, 'login.html', {'img_url': imagem_url})


def home(request):
    return render(request, 'base.html')


def pagina_inicial(request):
    fichas = [{"id": 1, "nome": "Ficha 1"}, {"id": 2, "nome": "Ficha 2"}, {"id": 3, "nome": "Ficha 3"}]
    return JsonResponse({'html': [render_to_string(
                'pagina_inicial.html',
                {'fichas': fichas, 'quantidade':  len(fichas)}
                )]
            })


def imagem_local(request, cod_img):
    if not cod_img:
        imagem_url = os.path.join('templates', 'images', 'bg-login.png')

    return FileResponse(open(imagem_url, 'rb'))


def abrir_ficha(request):
    return JsonResponse({'html': [render_to_string(
            'fichaAcidenteTrabalho.html',
            # {'fichas': fichas, 'quantidade':  len(fichas)}
            )]
        })
















