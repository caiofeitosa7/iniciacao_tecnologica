import json
import os

from django.http import FileResponse
from django.http import JsonResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from . import models


def login(request):
    imagem_url = imagem_local(request, 0)
    return render(request, 'login.html', {'img_url': imagem_url})


def home(request):
    return render(request, 'base.html')


def imagem_local(request, cod_img):
    if not cod_img:
        imagem_url = os.path.join('templates', 'images', 'bg-login.png')

    return FileResponse(open(imagem_url, 'rb'))


def pagina_inicial(request):
    fichas = models.get_formularios_ativos()

    return JsonResponse({'html': [render_to_string(
                'pagina_inicial.html',
                {'fichas': fichas, 'quantidade':  len(fichas)}
                )]
            })


def abrir_ficha(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        id_ficha = int(body['idFicha'])

        if id_ficha == 1:
            return JsonResponse({'html': [render_to_string('fichaNotificacaoGeral.html')]})
        elif id_ficha == 2:
            return JsonResponse({'html': [render_to_string('fichaAcidenteTrabalho.html')]})
        elif id_ficha == 3:
            return JsonResponse({'html': [render_to_string('fichaViolenciaInterpessoal.html')]})
        elif id_ficha == 4:
            return JsonResponse({'html': [render_to_string('fichaAntiRabica.html')]})


def set_ficha_notificacao(request):
    if request.method == 'POST':
        try:
            models.registrar_ficha_notificacao(json.loads(request.body))
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error'})
















