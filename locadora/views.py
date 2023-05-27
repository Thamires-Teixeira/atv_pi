from django.shortcuts import render
from django.http import HttpResponse
from .models import Locacao, Filme

# Create your views here.
def index (request):
    return render(request, "locadora/index.html")

def locacao (request):
    locacao = Locacao.objects.all()
    return render(request, "locadora/locacao.html", {'locacao': locacao})

def lista_filmes (request):
    filmes = Filme.objects.all()
    return render(request, "locadora/lista_filmes.html", {'filmes': filmes})
