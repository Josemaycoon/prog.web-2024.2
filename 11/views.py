from django.shortcuts import HttpResponse, render

# create your views here.

def index(request):
    return HttpResponse('A view index funcionou , wow!')

def sobre(request):
    return HttpResponse('<h1>Sistema 1.0 desenvolvido por mim<h1>')

def contato(request):
    return HttpResponse('Esta é a pagina de contato.')

def ajuda(request):
    return HttpResponse('Esta é a pagina de ajuda')    