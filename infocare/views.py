import json, string, os
from datetime import datetime

from django.http import HttpResponse
from django.http import FileResponse, JsonResponse
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from . import models

from django.core.files.storage import FileSystemStorage


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
        'quant_fichas_preliminares': models.get_quantidade_fichas('preliminar'),
        'quant_fichas_pendentes': models.get_quantidade_fichas('pendente'),
        'formularios': models.get_formularios_ativos()
    }

    return JsonResponse({
        'html': [render_to_string('pagina_inicial.html', contexto, request=request)],
        'status': 'success'
    })


def listagem_fichas(request, status: str, titulo: str, id_tabela: str):
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
        'preliminar',
        'NOTIFICAÇÕES PRELIMINARES',
        'tabelaNotificacoesPreliminares'
    )


def fichas_pendentes_view(request):
    return listagem_fichas(
        request,
        'pendente',
        'NOTIFICAÇÕES PENDENTES',
        'tabelaNotificacoesPendentes'
    )


def fichas_concluidas_view(request):
    return listagem_fichas(
        request,
        'concluida',
        'NOTIFICAÇÕES CONCLUÍDAS',
        'tabelaNotificacoesConcluidas'
    )


def abrir_formulario_view(request, codigo: int):
    arquivos_formulario: list[str] = [
        'fichaNotificacaoGeral.html',
        'fichaAcidenteTrabalho.html',
        'fichaViolenciaInterpessoal.html'
    ]

    if request.method == 'GET':
        contexto = {'cod_formulario': codigo}
        return JsonResponse({
            'html': [render_to_string(arquivos_formulario[codigo - 1], contexto, request=request)]
        })


def visualizar_ficha_view(request, cod_ficha: int, cod_formulario: int):
    if request.method == 'GET':
        request.session['ultimo_form_aberto'] = cod_formulario
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
            'status_ficha_aberta': request.session.get('status_ficha_aberta'),
            'quant_obs': models.get_quantidade_observacoes_abertas(cod_ficha),
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
                cod_ficha = models.set_ficha_notificacao(dados)
                return JsonResponse({
                    'cod_ficha': cod_ficha,
                    'status': 'success'
                })

        except Exception as e:
            return redirect(reverse('pagina_inicial'))

        return redirect(reverse('home'))


# def registrar_ficha_notificacao(request):
#     if request.method == 'POST':
#         dados = json.loads(request.body)
#
#         try:
#             if dados.get('codigo', False):
#                 args = {
#                     'cod_ficha': dados['codigo'],
#                     'cod_formulario': dados['cod_formulario'],
#                 }
#
#                 models.alterar_ficha(dados)
#                 return redirect(reverse('visualizar_ficha', kwargs=args))
#             else:
#                 models.set_ficha_notificacao(dados)
#                 return redirect(reverse('pagina_inicial'))
#
#         except Exception as e:
#             return redirect(reverse('pagina_inicial'))


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
        dados['cod_usuario_concluinte'] = request.session.get('cod_usuario')
        dados['dataHora_cadastro'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dados['dataHora_concluida'] = dados['dataHora_cadastro']
        models.set_observacao(dados)
        return redirect(reverse('observacoes', kwargs={'cod_ficha': dados['cod_ficha']}))


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


def upload_arquivos(request, cod_ficha):
    def salvarArquivo(chave):
        f = request.FILES[chave]
        fs = FileSystemStorage()
        filename = fs.save(str(f.name), f)
        uploaded_file_url = fs.url(filename)
        print(uploaded_file_url)

    if request.method == 'POST':
        print('chegou aqui:', request.FILES.keys())
        for key in request.FILES.keys():
            salvarArquivo(key)

        return redirect('home')












