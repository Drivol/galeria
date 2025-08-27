from django.shortcuts import render, get_object_or_404
from .models import Foto

def lista_fotos(request):
    busca = request.GET.get('q')
    if busca:
        fotos = Foto.objects.filter(titulo__icontains=busca) | Foto.objects.filter(descricao__icontains=busca)
    else:
        fotos = Foto.objects.all().order_by('-data_viagem')
    return render(request, 'fotos/lista.html', {'fotos': fotos})

def detalhe_foto(request, foto_id):
    foto = get_object_or_404(Foto, id=foto_id)
    return render(request, 'fotos/detalhe.html', {'foto': foto})
