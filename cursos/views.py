from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Curso
from datetime import datetime

# Create your views here.
def acessar_curso(request):
    return render(request, 'acessar_curso.html')     
                    # HttpResponse('Olá mundo!')

def listar_curso(request):
    return render(request, 'listar_curso.html')    

def criar_curso(request):
    if request.method == "GET":
        status = request.GET.get('status')

        return render(request, 'criar_curso.html', {'status': status})
    elif request.method == "POST":
        #print(request.POST.get('nome'))
        #print(request.POST.get('carga_horaria'))
        nome_digitado= request.POST.get('nome')
        carga_horaria_digitado = request.POST.get('carga_horaria')

        curso = Curso(
            nome= nome_digitado,
            carga_horaria=carga_horaria_digitado,
            data_criacao=datetime.now()
        )
        curso.save()

        return redirect('/curso/criar_curso/?status=1')
