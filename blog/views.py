from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Aluno

def index(request):
    nome = Aluno.objects.all()
    return render(request, 'index.html', {'nome': nome})

def carreira(request):
    descricao = Aluno.objects.all()
    return render(request, 'carreira.html', {'descricao': descricao})