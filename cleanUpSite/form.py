from django.core.exceptions import ValidationError
from django.forms import ModelForm
from cleanUpSite.models import Usuarios, Foruns
from django.contrib.auth.models import User

#class UsuariosForm(UserCreationForm):
#    class Meta:
#        model = Usuarios
#        fields = ['nome', 'email', 'senha']
#
#  estamos usando o módulo de autenticação do próprio django então não precisa mais disso aqui por enquanto
#  se for usar de novo tem que fazer as importações na views e descomentar tudo que tá lá
#  foi comentada nas configs a linha que colocava o módulo personalizado como o principal da autenticação
#  o arquivo da pasta backends ta inútil no momento com isso

from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

class CustomUserCreationForm(UserCreationForm):
    password = forms.CharField(
        label="Senha",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password'}),
    )
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) <= 6:
            raise ValidationError("A senha deve ter no mínimo 6 caracteres.")
        return password

    class Meta:
        model = User  # Certifique-se de que o modelo correto esteja sendo importado.
        fields = ['username', 'email', 'password']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # Liste os campos que os usuários podem atualizar




