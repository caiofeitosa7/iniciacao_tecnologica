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

    return JsonResponse({
        'html': [render_to_string('pagina_inicial.html', {'fichas': fichas})]
    })


def fichas_preliminares(request):
    if request.method == 'POST':
        pass
        # dados = json.loads(request.body)
        # dados = retirar_caracteres_especiais(dados)

    else:
        # fichas = models.get_notificacoes_preliminares()
        fichas = []

    contexto = {
        'fichas': fichas,
        'titulo': 'NOTIFICAÇÕES PRELIMINARES',
        'id_tabela': 'tabelaNotificacoesPreliminares'
    }
    return JsonResponse({
        'html': [render_to_string('listagem_fichas.html', contexto)]
    })


def fichas_pendentes(request):
    if request.method == 'POST':
        pass
        # dados = json.loads(request.body)
        # dados = retirar_caracteres_especiais(dados)

    else:
        # fichas = models.get_notificacoes_preliminares()
        fichas = []

    contexto = {
        'fichas': fichas,
        'titulo': 'NOTIFICAÇÕES PENDENTES',
        'id_tabela': 'tabelaNotificacoesPendentes'
    }
    return JsonResponse({
        'html': [render_to_string('listagem_fichas.html', contexto)]
    })


def fichas_concluidas(request):
    if request.method == 'POST':
        pass
        # dados = json.loads(request.body)
        # dados = retirar_caracteres_especiais(dados)

    else:
        # fichas = models.get_notificacoes_preliminares()
        fichas = []

    contexto = {
        'fichas': fichas,
        'titulo': 'NOTIFICAÇÕES CONCLUÍDAS',
        'id_tabela': 'tabelaNotificacoesConcluidas'
    }
    return JsonResponse({
        'html': [render_to_string('listagem_fichas.html', contexto)]
    })


def abrir_ficha(request, codigo: int):
    arquivos_ficha: list[str] = [
        'fichaNotificacaoGeral.html',
        'fichaAcidenteTrabalho.html',
        'fichaViolenciaInterpessoal.html'
    ]

    if request.method == 'GET':
        return JsonResponse({'html': [render_to_string(arquivos_ficha[codigo - 1])]})


def set_ficha_notificacao(request):
    if request.method == 'POST':
        try:
            models.registrar_ficha_notificacao(json.loads(request.body))
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error'})
