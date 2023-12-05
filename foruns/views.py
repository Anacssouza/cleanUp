import datetime

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from django.utils import timezone
from django.views.generic import ListView

from foruns.form import CriaForum
from cleanUpSite.models import Foruns, UserFor


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


            return redirect('forum'),
    else:
        data['db'] = Foruns.objects.order_by('-userfor__data_participacao').distinct()

        data['form'] = CriaForum()
        user = request.user
        data['user'] = user
        user_for = UserFor.objects.filter(id_foruns_id=15).first()
        author_name = user_for.user.username
        data['author_name'] = author_name
        data_participacao = user_for.data_participacao
        data['datap'] = data_participacao

        for forum in data['db']:
            user_for = UserFor.objects.filter(id_foruns=forum.pk).first()
            author_name = user_for.user.username if user_for else "anonimo"
            datap = user_for.data_participacao if user_for else "sem data registrada"
            forum.author_name = author_name
            forum.data_participacao = datap

    #paginação
    post_list = Foruns.objects.all()
    paginator = Paginator(post_list, 5)  # Crie o objeto Paginator
    page = request.GET.get('page')
    posts = paginator.get_page(page)  # Obtenha a página atual
    data['pg'] = posts


    return render(request, 'forum.html', data)

def criaF(request):

    form = CriaForum(request.POST or None)
    user = request.user
    if form.is_valid():
        form.save(user)
        return redirect('forum')


def excluiF(request, pk):

        try:
            user = Foruns.objects.get(pk=pk)
            user.delete()
        except:
            pass
        return redirect('forum')


def editarF(request, pk):
    forum = Foruns.objects.get(pk=pk)
    if request.method == 'POST':
        form = CriaForum(request.POST)
        if form.is_valid():
            forum.titulo = form.cleaned_data['titulo']
            forum.descricao = form.cleaned_data['descricao']
            forum.save()
            return redirect('forum')
    else:
        form = CriaForum(initial={'titulo': forum.titulo, 'descricao': forum.descricao})

    return render(request, 'forum.html', {'form': form})
