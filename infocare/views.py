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


def pagina_inicial_view(request):
    formularios = models.get_formularios_ativos()

    return JsonResponse({
        'html': [render_to_string('pagina_inicial.html', {'formularios': formularios})]
    })


def fichas_preliminares(request):
    if request.method == 'POST':
        pass
        # dados = json.loads(request.body)
        # dados = retirar_caracteres_especiais(dados)

    else:
        fichas = models.listar_fichas(status='preliminar')

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
        fichas = models.listar_fichas(status='pendente')

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
        fichas = models.listar_fichas(status='concluida')

    contexto = {
        'fichas': fichas,
        'titulo': 'NOTIFICAÇÕES CONCLUÍDAS',
        'id_tabela': 'tabelaNotificacoesConcluidas'
    }
    return JsonResponse({
        'html': [render_to_string('listagem_fichas.html', contexto)]
    })


def abrir_formulario_view(request, codigo: int):
    arquivos_formulario: list[str] = [
        'fichaNotificacaoGeral.html',
        'fichaAcidenteTrabalho.html',
        'fichaViolenciaInterpessoal.html'
    ]

    if request.method == 'GET':
        return JsonResponse({'html': [render_to_string(arquivos_formulario[codigo - 1])]})


def visualizar_ficha_view(request, cod_ficha: int, cod_formulario: int):
    contexto = {'ficha': models.get_ficha(cod_ficha, cod_formulario)}
    arquivos_ficha: list[str] = [
        'editar_fichaNotificacaoGeral.html',
        'editar_fichaAcidenteTrabalho.html',
        'editar_fichaViolenciaInterpessoal.html'
    ]

    if request.method == 'GET':
        arquivo_html = os.path.join('edicao', arquivos_ficha[cod_formulario - 1])
        return JsonResponse({
            'html': [render_to_string(arquivo_html, contexto)],
            'status': 'success'
        })


def registrar_ficha_notificacao(request):
    if request.method == 'POST':
        try:
            models.set_ficha_notificacao(json.loads(request.body))
            return JsonResponse({'status': 'success'})
        except Exception as e:
            return JsonResponse({'status': 'error'})
