from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect, reverse
from django.template.loader import render_to_string
from django.http import FileResponse, JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from datetime import datetime, timedelta
from django.http import HttpResponse
from django.contrib import messages
from . import models
import tempfile
import zipfile
import json
import csv
import os


def login(request):
    imagem_url = imagem_local(request, 0)
    return render(request, 'login.html', {'img_url': imagem_url})


def home(request):
    if not request.session.get('acesso_usuario'):
        return redirect(reverse('login'))

    contexto = {
        'acesso_usuario': request.session.get('acesso_usuario'),
        'formularios': models.get_tipos_ficha_ativos()
    }
    return render(request, 'base.html', contexto)


def imagem_local(request, cod_img):
    if not cod_img:
        imagem_url = os.path.join('templates', 'images', 'bg-login.png')
    else:
        imagem_url = os.path.join('templates', 'images', 'brasao-da-republica.png')
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
    if request.method == 'POST':    # fazer filtro
        pass
        # dados = json.loads(request.body)
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
        contexto = {
            'cod_formulario': codigo,
            'nome_usuario': request.session.get('nome_completo_usuario')
        }
        return JsonResponse({
            'html': [render_to_string(html, contexto, request=request)]
        })


def visualizar_ficha_view(request, cod_ficha: int, cod_formulario: int):
    if request.method == 'GET':
        dados = models.get_ficha(cod_ficha)
        html = models.get_html_tipo_ficha(cod_formulario)
        arquivo_html = os.path.join('edicao', 'editar_' + html)
        request.session['ultimo_form_aberto'] = cod_formulario
        contexto = {
            'ficha': dados,
            'acesso_usuario': request.session.get('acesso_usuario'),
            'status_ficha_aberta': request.session.get('status_ficha_aberta'),
            'visualizadores': models.get_visualizacoes_ficha(cod_ficha)
        }

        models.set_visualizacao_ficha(cod_ficha, request.session['cod_usuario'])

        return JsonResponse({
            'html': [render_to_string(arquivo_html, contexto)],
            'status': 'success'
        })


def registrar_ficha(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        cod_usuario = int(request.session.get('cod_usuario'))

        # try:
        if dados.get('codigo', False):  # Se exitir, significa que é uma atualizacao
            args = {
                'cod_ficha': dados['codigo'],
                'cod_formulario': dados['cod_tipo_ficha'],
            }

            cod_ficha = models.alterar_ficha(dados)
            if cod_ficha:
                messages.success(request, 'Ficha atualizada com sucesso!')
                return JsonResponse({
                    'status': 'success',
                    'cod_ficha': cod_ficha,
                    # 'edicao_ficha': 1,
                    'view_visualizacao': reverse('visualizar_ficha', kwargs=args)
                })
        else:
            numero_ficha = dados.get('numero-ficha', False)

            if numero_ficha and models.numero_ficha_existe(numero_ficha):
                return JsonResponse({
                    'status': 'erro-numero-ficha'
                })

            cod_ficha = models.set_ficha(dados, cod_usuario)
            if cod_ficha:
                messages.success(request, 'Ficha cadastrada com sucesso!')
                return JsonResponse({
                    'cod_ficha': cod_ficha,
                    'status': 'success',
                    # 'edicao_ficha': 0
                })

        return JsonResponse({
            'status': 'error'
        })

        # except Exception as e:
        #     print(e)
        #     return redirect(reverse('pagina_inicial'))


def pendencias_view(request, cod_ficha):
    contexto = {
        'cod_ficha': cod_ficha,
        'status_ficha_aberta': request.session.get('status_ficha_aberta'),
        'cod_formulario': request.session.get('ultimo_form_aberto'),
        'cod_usuario': request.session.get('cod_usuario'),
        'pendencias': models.listar_pendencias(cod_ficha)
    }
    return JsonResponse({
        'html': [render_to_string('pendencias.html', contexto, request=request)],
        'status': 'success'
    })


def registrar_pendencia(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        dados['cod_usuario'] = int(request.session.get('cod_usuario'))
        dados['cod_usuario_concluinte'] = int(request.session.get('cod_usuario'))
        dados['dataHora_cadastro'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        dados['dataHora_concluida'] = dados['dataHora_cadastro']
        models.set_pendencia(dados)

        return redirect(reverse(
            'pendencias',
            kwargs={
                'cod_ficha': dados['cod_ficha']
            }
        ))


def fechar_pendencia(request, cod_ficha: int, cod_pendencia: int):
    if request.method == 'GET':
        dados = {
            'cod_pendencia': cod_pendencia,
            'dataHora_concluida': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'cod_usuario_concluinte': request.session.get('cod_usuario')
        }

        models.fechar_pendencia(dados)
        return redirect(reverse(
            'pendencias',
            kwargs={
                'cod_ficha': cod_ficha
            }
        ))


def marcar_ficha_concluida(request, cod_ficha: int):
    if request.method == 'GET':
        models.set_ficha_concluida(cod_ficha)
        messages.success(request, 'Ficha concluida!')
        return redirect(reverse('fichas_preliminares'))


def marcar_ficha_preliminar(request, cod_ficha: int, estado_ficha: int):
    if request.method == 'GET':
        models.set_ficha_preliminar(cod_ficha)

        if estado_ficha == 4:
            return redirect(reverse('fichas_pendentes'))
        else:
            messages.success(request, 'A ficha foi restaurada para NOTIFICAÇÕES PRELIMINARES!')
            return redirect(reverse('fichas_descartadas'))


def marcar_ficha_descartada(request, cod_ficha: int):
    if request.method == 'GET':
        models.set_ficha_descartada(cod_ficha)
        messages.success(request, 'Ficha descartada com sucesso!')
        return redirect(reverse('fichas_preliminares'))


@api_view(['POST'])
@permission_classes([AllowAny])
def upload_arquivos(request, cod_ficha: int):
    # redirecionamento = request.POST.get('redirecionamento')
    # print(redirecionamento)

    if request.session.get('cod_usuario') is not None:
        registros = []
        for key in request.FILES.keys():
            diretorio = 'arquivos'
            arquivo = request.FILES[key]
            nome_original = arquivo.name.split('.')[0]
            nome_armazenado = nome_original + datetime.now().strftime('_%f')
            extensao = '.' + arquivo.name.split('.')[-1]
            data_cadastro = datetime.now().strftime('%Y-%m-%d')
            data_deletado = None
            deletado = 0

            fs = FileSystemStorage()
            filename = fs.save(os.path.join(diretorio, nome_armazenado + extensao), arquivo)
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
                0
            ))

        if registros:
            models.set_arquivos_ficha(registros, cod_ficha)

        # if redirecionamento:
        #     return redirect(redirecionamento)
        return redirect('home')
    else:
        return redirect('login')


def verificar_numero_ficha_existe(request, numero: int) -> int:
    """
        Verifica se o número da ficha já existe no banco de dados
        :param request:
        :param numero:
        :return: Bool
    """

    return JsonResponse({
        'numero_existe': models.numero_ficha_existe(numero)
    })


def obter_info_paciente(request, prontuario: int):
    """
        Retorna as informações básicas do paciente
        :param request:
        :param prontuario:
        :return: JSON
    """

    dados = models.get_info_comum_paciente(prontuario)
    return JsonResponse({
            'status': 'success' if dados else 'erro',
            'dados': dados if dados else {}
        })


def download_fichas(request):
    """
    Faz o ‘download’ das fichas do tipo selecionado em um determinado período.
    :param request:
    :return: ZIP contendo os arquivos CSV.
    """

    dados = request.POST
    fichas = models.listar_fichas_download(dados)

    # Criar um diretório temporário para armazenar os CSVs
    temp_dir = tempfile.mkdtemp()
    zip_filename = ''

    try:
        csv_files = []
        for codigo in fichas:
            dados_ficha = models.get_ficha(codigo)
            dados_ficha.pop('quant_pendencias', None)
            dados_ficha.pop('arquivos', None)

            # Definir o caminho do arquivo CSV
            csv_filename = os.path.join(temp_dir, f'ficha_{codigo}.csv')
            csv_files.append(csv_filename)

            # Criar o arquivo CSV no disco
            with open(csv_filename, 'w', newline='') as csv_file:
                writer = csv.writer(csv_file)
                writer.writerow(dados_ficha.keys())
                writer.writerow(dados_ficha.values())

        # Criar um arquivo ZIP temporário no disco
        zip_filename = os.path.join(temp_dir, 'fichas.zip')
        with zipfile.ZipFile(zip_filename, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for csv_file in csv_files:
                zip_file.write(csv_file, os.path.basename(csv_file))

        # Abrir o ZIP para leitura e enviar como resposta
        with open(zip_filename, 'rb') as zip_file:
            response = HttpResponse(zip_file.read(), content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="fichas.zip"'

        return response

    finally:
        # Apagar todos os arquivos temporários
        for csv_file in csv_files:
            os.remove(csv_file)
        os.remove(zip_filename)
        os.rmdir(temp_dir)
