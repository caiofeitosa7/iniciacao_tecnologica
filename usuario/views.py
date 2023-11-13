from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
import json


def listar_usuarios(request):
    if request.method == 'GET':
        usuarios = ['Caio',  'João', 'Maria',  'José',  'Ana']
        html = render_to_string('usuarios.html', {'usuarios': usuarios})

        return JsonResponse({'html': [html]})


def logar_usuario(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        usuario = body['usuario']
        senha = body['senha']

        if usuario == 'admin' and senha == '123':
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'error'})

















