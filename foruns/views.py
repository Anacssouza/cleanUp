import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from django.utils import timezone

from foruns.form import CriaForum
from cleanUpSite.models import Foruns


# Create your views here.

@login_required(login_url="home")
def forum(request):
    data = {}
    form = CriaForum(request.POST)
    if request.method == 'POST':
        # Se o formulário for submetido, lide com a criação do fórum aqui
        if form.is_valid():
            user = request.user
            form.save(user)
            # Processar e salvar os dados do formulário, por exemplo:
            # novo_forum = form.save(commit=False)
            # novo_forum.save()
            # Redirecione para a página de fórum ou faça outra ação após criar o tópico.
            return redirect('forum'),
    else:
        # Se for uma solicitação GET, mostre a página do fórum com o formulário de criação
        data['db'] = Foruns.objects.all()
        data['form'] = CriaForum()
        user = request.user
        data['user'] = user

    return render(request, 'forum.html', data)

def criaF(request):

    form = CriaForum(request.POST or None)
    user = request.user
    if form.is_valid():
        form.save(user)
        return redirect('forum')