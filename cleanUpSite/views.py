from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail, EmailMultiAlternatives
from django.shortcuts import render, redirect,get_object_or_404
from django.template.loader import render_to_string
from django.utils.html import strip_tags

from cleanUpSite.form import CustomUserChangeForm, CustomUserCreationForm, foto
from cleanUpSite.models import Foruns
from django.contrib import messages
from django.contrib.auth import get_user
#from cleanUpSite.urls import handler404

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

        if len(senha) < 8:
            return render(request, 'home.html', {
                'error': 'A senha deve ter pelo menos 8 caracteres'
            })

        user = User.objects.filter(email=email).first()

        if user:
            return render(request, 'home.html', {
                'error': 'E-mail já existe'
            })


        user = User.objects.create_user(username=username, email=email, password=senha)
        user.save()
        login(request, user)
        return render(request, 'minhaConta.html')
"""

def create(request):
    form = CustomUserCreationForm(request.POST or None)
    if form.is_valid():
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        user = User.objects.filter(email=email).first()
        if user:
            return render(request, 'home.html', {
                'error': 'E-mail já existe'
            })
        user = User.objects.create_user(username=username, email=email, password=senha)
        User.save()
        login(request, user)
        return render(request, 'minhaConta.html')
"""
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


def upload_profile_picture(request):
    if request.method == 'POST':
        form = foto(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('página_de_sucesso')
    else:
        form = foto()

    return render(request, 'minhaConta.html', {'form': form})

@login_required(login_url="home")
def minhaConta(request):
    user = request.user
    return render(request, 'minhaConta.html', {'user': user})

def sair(request):
    logout(request)
    return redirect('home')
# exclui o arquivo sair.html tem q testar se não quebrou nada

def editar(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()

            # Redirecione para a página de perfil ou outra página após a atualização
    else:
        form = CustomUserChangeForm(instance=request.user)

    return render(request, 'minhaConta.html', {'form': form})

def deletarUsuario(request, pk):
    try:
        user = User.objects.get(pk=pk)
        user.delete()
    except:
        # Trate o caso em que o usuário não existe
        pass
    return redirect('home')

@login_required
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('minhaConta')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})

def contato(request):
    return render(request, 'contato.html')

def enviaemail (request):
    nome = request.POST.get('name')
    email = request.POST.get('email')
    mensagem = request.POST.get('message')
    print(mensagem)

    texto = f'nome = {nome}, email = {email}, mensagem = {mensagem}'

    html_content = render_to_string('emails/emailContato.html', {'nome': nome, 'email': email, 'mensagem': mensagem})
    text_content = strip_tags(html_content)

    email = EmailMultiAlternatives('CleanUp - Chegou uma mensagem de contato', text_content, 'anacsilveirasouzareserva@gmail.com', ['anacsilveirasouza@gmail.com'])
    email.attach_alternative(html_content, 'text/html')
    email.send()

    return redirect('home')

def custom_404_page(request, exception):
    return render(request, '404.html', status=404)

def custom_500_page(request):
    return render(request, '500.html', status=500)

def teste404(request):
    return render(request, '404.html')

def teste500(request):
    return render(request, '500.html')

def conteudos(request):
    return render(request, 'conteudos.html')