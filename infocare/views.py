from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string


def home(request):
    return render(request, 'base.html')


def pagina_inicial(request):
    return JsonResponse({'html': [render_to_string('pagina_inicial.html')]})




















