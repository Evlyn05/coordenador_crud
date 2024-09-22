from django.shortcuts import render, redirect
from .models import Coodenador
from .forms import CoodenadorForm


# Create your views here.
def index(request):
    coodenadores = Coodenador.objects.all()
    contexto = {
        'coodenadores': coodenadores
    }
    return render(request,'core/index.html',contexto)

def lista(request):
    coodenadores = Coodenador.objects.all()
    contexto = {
        'coodenadores': coodenadores
    }
    return render(request,'core/lista.html',contexto)


def cadastro(request):
    form = CoodenadorForm()
    if request.method == 'POST':
        form = CoodenadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_coodenador')
        
        form = CoodenadorForm()
    contexto={
             'form': form
    }  
    return render(request,'core/form.html',contexto)

def editar_coodenador(request,id):
    coodenador = Coodenador.objects.get(id=id)

    if request.method == 'POST':
        form = CoodenadorForm(request.POST,instance=coodenador)
        if form.is_valid():
            form.save()
            return redirect('lista_coodenador')
    else:
        form = CoodenadorForm(instance=coodenador)

    contexto={
            'form':form
    }
    return render(request,'core/form.html',contexto)
        
def remover_coodenador(request,id):
    coodenador = Coodenador.objects.get(id=id)
    coodenador.delete()
    return redirect('lista_coodenador')

    

