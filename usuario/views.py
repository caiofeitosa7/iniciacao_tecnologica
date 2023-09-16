from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


def teste(request):
    return HttpResponse('Hello World')


def listar_usuarios(request):
    if request.method == 'GET':
        usuarios = ['Caio',  'João', 'Maria',  'José',  'Ana']
        html = render_to_string('usuarios.html', {'usuarios': usuarios})

        return JsonResponse({'html': [html]})


















