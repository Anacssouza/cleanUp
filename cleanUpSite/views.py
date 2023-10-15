from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect,get_object_or_404
from cleanUpSite.form import CriaForum
from cleanUpSite.models import Foruns
from django.contrib import messages
from django.contrib.auth import get_user
def inicial(request):
    return render(request, 'inicial.html')


#mudei aqui
def home(request):
    data = {}
    #data['form'] = UsuariosForm()
    data['form'] = User
    return render(request, 'home.html', data)

#cadastro
def create(request):
 #   form = UsuariosForm(request.POST or None)
  #  if form.is_valid():
  #      form.save()
  #      return redirect('inicial')
    if request.method == 'GET':
      return render(request, 'home.html')
    else:
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        user = User.objects.filter(email=email).first()

        if user:
            return render(request, 'home.html', {
                'error': 'E-mail já existe'
            })

        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        login(request, user)
        return render(request, 'minhaConta.html')

#login
def login_site(request):

    if request.method == 'GET':
        return render(request,'home.html')
    else:
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = authenticate(username=username, password=senha)
        print(user)

        if user:
            login(request, user)
            return render(request, 'minhaConta.html')
        else:
            return render(request, 'home.html', {
                'error': 'Dados errados'
            })

""" if request.method == 'GET':
        return render(request,'desmatamento',{
            'form': UsuariosForm
        })
    else:
        user = authenticate(
            request, email=request.POST['email'],
            password=request.POST['password']
        )

        if user is None:
            return render(request, 'home.html', {
                'form': UsuariosForm,
                'error': 'E-mail ou senha está incorreto'
            })
        else:
            login(request, user)
            return redirect('desmatamento')
"""

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

@login_required(login_url="home")
def minhaConta(request):
    user = request.user
    return render(request, 'minhaConta.html', {'user': user})

def sair(request):
    logout(request)
    return redirect('home')
# exclui o arquivo sair.html tem q testar se não quebrou nada

def editar(request, username):
    cliente = User.objects.get(username=username)
    form = User.objects.create_user(request.POST or None, instance=cliente)
    if str(request.method) == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso!')
            return render(request, 'minhaConta.html', {'cliente': cliente})
        else:
            messages.error(request, 'Erro ao alterar o contato')
    context = {
        'form': form,
        'cliente': cliente
    }
    return render(request, 'minhaConta.html', context)
