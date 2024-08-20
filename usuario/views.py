from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import json, string

from . import models


def logout(request):
    request.session.flush()
    return redirect('login')


def logar_usuario(request):
    logado = False

    if request.method == 'POST':
        body = json.loads(request.body)
        usuario = body['usuario']
        senha = body['senha']

        for usuario_bd in models.listar_usuarios():
            if usuario == usuario_bd['usuario'] and senha == usuario_bd['senha']:
                request.session['nome_usuario'] = usuario_bd['nome'].split(' ')[0].capitalize()
                request.session['acesso_usuario'] = usuario_bd['tipo_acesso']
                request.session['cod_usuario'] = usuario_bd['codigo']
                logado = True
                break

        if logado:
            return JsonResponse({'status': 'success'})
        else:
            messages.warning(request, 'Usuário ou senha incorretos!')
            return JsonResponse({'status': 'danger'})


def usuarios_view(request):
    if request.method == 'GET':
        usuarios = models.listar_usuarios()
        return JsonResponse({
            'html': [render_to_string('usuarios.html', {'usuarios': usuarios})],
            'status': 'success'
        })


def cadastrar_usuario_view(request):
    contexto = {
        'acessos': models.listar_acessos()
    }

    return JsonResponse({
        'html': [
            render_to_string(
                'cadastrar_usuario.html',
                context=contexto,
                # request=request
            )
        ],
        'status': 'success'
    })


def registrar_usuario(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        dados['acesso'] = int(dados['acesso'])

        if dados.get('codigo', False):
            models.atualizar_usuario(dados)
            return redirect(reverse(
                'visualizar_usuario',
                kwargs={'codigo': dados['codigo']}
            ))
        else:
            models.set_usuario(dados)
            return redirect('usuarios')


def visualizar_usuario_view(request, codigo):
    if request.method == 'GET':
        usuario = models.get_usuario(codigo)
        contexto = {
            'usuario': usuario,
            'acessos': models.listar_acessos()
        }

        return JsonResponse({
            'html': [render_to_string('visualizar_usuario.html', contexto)],
            'status': 'success'
        })


def apagar_usuario(request, codigo):
    if request.method == 'GET':
        models.apagar_usuario(codigo)
        return JsonResponse({
            'status': 'success'
        })








