from django.shortcuts import render, get_object_or_404, redirect
from .forms import NotaForm
from .models import Nota
# Create your views here.
def lista_notas(request):
    notas = Nota.objects.all()
    return render(request, 'notas_app/lista_notas.html', {'notas': notas})

def crear_nota(request):
    if request.method == 'POST':
        form = NotaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm()
    return render(request, 'notas_app/crear_nota.html', {'form': form})

def editar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        form = NotaForm(request.POST, instance=nota)
        if form.is_valid():
            form.save()
            return redirect('lista_notas')
    else:
        form = NotaForm(instance=nota)
    return render(request, 'notas_app/editar_nota.html', {'form': form})

def eliminar_nota(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    nota.delete()
    return redirect('lista_notas')