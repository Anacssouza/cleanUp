from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from foruns.form import CriaForum
from cleanUpSite.models import Foruns


# Create your views here.

@login_required(login_url="home")
def forum(request):
    data = {}
    if request.method == 'POST':
        # Se o formulário for submetido, lide com a criação do fórum aqui
        form = CriaForum(request.POST)
        if form.is_valid():
            # Processar e salvar os dados do formulário, por exemplo:
            # novo_forum = form.save(commit=False)
            # novo_forum.save()
            # Redirecione para a página de fórum ou faça outra ação após criar o tópico.
            return redirect('forum')
    else:
        # Se for uma solicitação GET, mostre a página do fórum com o formulário de criação
        data['db'] = Foruns.objects.all()
        data['form'] = CriaForum()

    return render(request, 'forum.html', data)

def criaF(request):
    form = CriaForum(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('forum')