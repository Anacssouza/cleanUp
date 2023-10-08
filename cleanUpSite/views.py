from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


from django.shortcuts import render, redirect
from cleanUpSite.form import UsuariosForm, CriaForum
from cleanUpSite.models import Usuarios, Foruns

# Create your views here.
def inicial(request):
    return render(request, 'inicial.html')


#mudei aqui
def home(request):
    data = {}
    data['form'] = UsuariosForm()
    return render(request, 'home.html', data)

def create(request):
    form = UsuariosForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('inicial')

def sigin(request):

    if request.method == 'GET':
        return render(request,'desmatamento',{
            'form': UsuariosForm
        })
    else:
        user = authenticate(
            request, email=request.POST['email'], password=request.POST['password']
        )

        if user is None:
            return render(request, 'home.html', {
                'form': UsuariosForm,
                'error': 'E-mail ou senha está incorreto'
            })
        else:
            login(request, user)
            return redirect('desmatamento')

#até aqui

def desmatamento(request):
    return render(request, 'desmatamento.html')

def lixao(request):
    return render(request, 'lixao.html')

def tema3(request):   # mudar depois
    return render(request, 'tema3.html')

""" apaguei aqui e apaguei uma rota no urls
def forum(request):
    data = {}
    data['db'] = Foruns.objects.all()
    return render(request, 'forum.html', data)

def criaForum(request):
    data = {}
    data['form'] = CriaForum()
    return render(request, 'criaForum.html', data)"""


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

def minhaConta(request, pk):
    data = {}
    data['db'] = Usuarios.objects.get(pk=pk)
    return render(request, 'minhaConta.html', data)

def sair(request):
    logout(request)
    return redirect('home')
# exclui o arquivo sair.html tem q testar se não quebrou nada
