from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.http import FileResponse, JsonResponse
from datetime import datetime, timedelta
from . import models
import json
import os


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
    contexto = {
        'quant_fichas_preliminares': models.get_quantidade_fichas(1),
        'quant_fichas_pendentes': models.get_quantidade_fichas(4),
        'formularios': models.get_tipos_ficha_ativos()
    }

    return JsonResponse({
        'html': [render_to_string('pagina_inicial.html', contexto, request=request)],
        'status': 'success'
    })


def listagem_fichas(request, status: int, titulo: str, id_tabela: str):
    if request.method == 'POST':
        pass
        # dados = json.loads(request.body)
        # dados = retirar_caracteres_especiais(dados)
    else:
        request.session['status_ficha_aberta'] = status
        fichas = models.listar_fichas(status)

    contexto = {
        'fichas': fichas,
        'titulo': titulo,
        'id_tabela': id_tabela,
        'status_fichas': status,
    }
    return JsonResponse({
        'html': [render_to_string('listagem_fichas.html', contexto, request=request)]
    })


def fichas_preliminares_view(request):
    return listagem_fichas(
        request,
        1,
        'NOTIFICAÇÕES PRELIMINARES',
        'tabelaNotificacoesPreliminares'
    )


def fichas_pendentes_view(request):
    return listagem_fichas(
        request,
        4,
        'NOTIFICAÇÕES PENDENTES',
        'tabelaNotificacoesPendentes'
    )


def fichas_concluidas_view(request):
    return listagem_fichas(
        request,
        2,
        'NOTIFICAÇÕES CONCLUÍDAS',
        'tabelaNotificacoesConcluidas'
    )


def fichas_descartadas_view(request):
    return listagem_fichas(
        request,
        3,
        'NOTIFICAÇÕES DESCARTADAS',
        'tabelaNotificacoesDescartadas'
    )


def abrir_formulario_view(request, codigo: int):
    html = models.get_html_tipo_ficha(codigo)

    if request.method == 'GET':
        contexto = {'cod_formulario': codigo}
        return JsonResponse({
            'html': [render_to_string(html, contexto, request=request)]
        })


def visualizar_ficha_view(request, cod_ficha: int, cod_formulario: int):
    if request.method == 'GET':
        request.session['ultimo_form_aberto'] = cod_formulario
        dados = models.get_ficha(cod_ficha)
        html = models.get_html_tipo_ficha(cod_formulario)
        arquivo_html = os.path.join('edicao', 'editar_' + html)
        contexto = {
            'ficha': dados,
            'status_ficha_aberta': request.session.get('status_ficha_aberta')
        }
        return JsonResponse({
            'html': [render_to_string(arquivo_html, contexto)],
            'status': 'success'
        })


def registrar_ficha(request):
    if request.method == 'POST':
        dados = json.loads(request.body)

        try:
            if dados.get('codigo', False):
                args = {
                    'cod_ficha': dados['codigo'],
                    'cod_formulario': dados['cod_tipo_ficha'],
                }

                cod_ficha = models.alterar_ficha(dados)
                return redirect(reverse('visualizar_ficha', kwargs=args))
            else:
                cod_ficha = models.set_ficha(dados)

                if cod_ficha:
                    return JsonResponse({
                        'cod_ficha': cod_ficha,
                        'status': 'success'
                    })

                return JsonResponse({
                    'status': 'error'
                })

        except Exception as e:
            print(e)
            return redirect(reverse('pagina_inicial'))


def observacoes_view(request, cod_ficha):
    contexto = {
        'cod_ficha': cod_ficha,
        'status_ficha_aberta': request.session.get('status_ficha_aberta'),
        'cod_formulario': request.session.get('ultimo_form_aberto'),
        'cod_usuario': request.session.get('cod_usuario'),
        'observacoes': models.listar_observacoes(cod_ficha)
    }
    return JsonResponse({
        'html': [render_to_string('observacoes.html', contexto, request=request)],
        'status': 'success'
    })


def registrar_observacao(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        dados['cod_usuario'] = int(request.session.get('cod_usuario'))
        dados['cod_usuario_concluinte'] = int(request.session.get('cod_usuario'))
        dados['dataHora_cadastro'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dados['dataHora_concluida'] = dados['dataHora_cadastro']
        models.set_observacao(dados)

        return redirect(reverse(
            'observacoes',
            kwargs={
                'cod_ficha': dados['cod_ficha']
            }
        ))


def fechar_observacao(request, cod_ficha, cod_obs):
    if request.method == 'GET':
        dados = {
            'cod_observacao': cod_obs,
            'dataHora_concluida': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_usuario_concluinte': request.session.get('cod_usuario')
        }

        models.fechar_observacao(dados)
        return redirect(reverse('observacoes', kwargs={'cod_ficha': cod_ficha}))


def marcar_ficha_concluida(request, cod_ficha):
    if request.method == 'GET':
        models.set_ficha_concluida(cod_ficha)
        return redirect(reverse('fichas_preliminares'))


def marcar_ficha_preliminar(request, cod_ficha):
    if request.method == 'GET':
        models.set_ficha_preliminar(cod_ficha)
        return redirect(reverse('fichas_pendentes'))


def marcar_ficha_descartada(request, cod_ficha):
    if request.method == 'GET':
        models.set_ficha_descartada(cod_ficha)
        return redirect(reverse('fichas_descartadas'))


def upload_arquivos(request, cod_ficha):
    if request.method == 'POST':

        registros = []
        for key in request.FILES.keys():
            diretorio = 'arquivos'
            arquivo = request.FILES[key]
            nome_original = arquivo.name.split('.')[0]
            nome_armazenado = datetime.now().strftime('%Y%m%d_%H%M%S_%f')
            extensao = '.' + arquivo.name.split('.')[-1]
            data_cadastro = datetime.now().strftime('%Y-%m-%d')
            data_deletado = None
            deletado = 0

            fs = FileSystemStorage()
            filename = fs.save(os.path.join(diretorio, nome_armazenado+extensao), arquivo)
            url_arquivo = fs.url(filename)

            registros.append((
                nome_original,
                nome_armazenado,
                extensao,
                url_arquivo,
                data_cadastro,
                data_deletado,
                deletado,
                cod_ficha,
            ))

        models.set_arquivos_ficha(registros)
        return redirect('home')















