from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def acessar_curso(request):
    return render(request, 'acessar_curso.html')     
                    # HttpResponse('Olá mundo!')

def criar_curso(request):
    if request.method == "GET":
        return render(request, 'criar_curso.html')
    elif request.method == "POST":
        #print(request.POST.get('nome'))
        #print(request.POST.get('carga_horaria'))
        nome = request.POST.get('nome')
        carga_horaria = request.POST.get('carga_horaria')
        
        return HttpResponse(f'{nome} - {carga_horaria}')
