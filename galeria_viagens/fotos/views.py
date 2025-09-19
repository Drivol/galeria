from django.shortcuts import render, get_object_or_404, redirect
from .models import Foto
from django.urls import reverse
from django.core.mail import send_mail
from .forms import ContatoForm

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

def contato(request):
    if request.method == 'POST':

        form = ContatoForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data['nome']
            email = form.cleaned_data['email']
            mensagem = form.cleaned_data['mensagem']

            send_mail(
                f'Mensagem de {nome}',
                f'Mensagem de {nome} ({email}):\n\n{mensagem}', email, ['seu_email_para_receber@exemplo.com'], fail_silently= False
            )

            return redirect(reverse('sucesso'))
    else:
        form = ContatoForm()

    return render(request, 'fotos/contato.html', {'form' : form})

def sucesso(request):
    return render(request, 'fotos/sucesso.html')

def sobre_nos(request):
 
    return render(request, 'fotos/sobre_nos.html')