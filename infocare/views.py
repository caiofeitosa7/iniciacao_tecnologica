import json, string, os
from datetime import datetime

from django.http import FileResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
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
        'html': [render_to_string('pagina_inicial.html', {'formularios': formularios})],
        'status': 'success'
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
    if request.method == 'GET':
        dados = models.get_ficha(cod_ficha, cod_formulario)
        arquivos_ficha: list[str] = [
            'editar_fichaNotificacaoGeral.html',
            'editar_fichaAcidenteTrabalho.html',
            'editar_fichaViolenciaInterpessoal.html'
        ]

        for key in dados.keys():
            if 'dt' in key and dados[key]:
                dados[key] = '-'.join(dados[key].split('/')[::-1])

        arquivo_html = os.path.join('edicao', arquivos_ficha[cod_formulario - 1])
        contexto = {
            'ficha': dados,
            'quant_obs': models.get_quantidade_observacoes(cod_ficha),
        }
        return JsonResponse({
            'html': [render_to_string(arquivo_html, contexto)],
            'status': 'success'
        })


def registrar_ficha_notificacao(request):
    if request.method == 'POST':
        dados = json.loads(request.body)

        try:
            if dados.get('codigo', False):
                args = {
                    'cod_ficha': dados['codigo'],
                    'cod_formulario': dados['cod_formulario'],
                }

                models.alterar_ficha(dados)
                return redirect(reverse('visualizar_ficha', kwargs=args))
            else:
                models.set_ficha_notificacao(dados)
                return redirect('home')

        except Exception as e:
            return redirect('pagina_inicial')


def observacoes_view(request, cod_ficha):
    contexto = {
        'cod_usuario': request.session.get('cod_usuario'),
        'observacoes': models.listar_observacoes(cod_ficha)
    }
    return JsonResponse({
        'html': [render_to_string('observacoes.html', contexto)],
        'status': 'success'
    })


def registrar_observacao(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        dados['dataHora_cadastro'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dados['dataHora_concluida'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        models.set_observacao(dados)
        return redirect(reverse('observacoes', kwargs={'cod_ficha': dados['cod_ficha']}))


















