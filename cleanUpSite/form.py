from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from cleanUpSite.models import Usuarios, Foruns, CustomUser
from django.contrib.auth.models import User


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
        model = User
        fields = ['username', 'email', 'password']


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class foto(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['profile_picture']

