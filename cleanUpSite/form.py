from django.forms import ModelForm
from cleanUpSite.models import Usuarios, Foruns

class UsuariosForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nome', 'email', 'senha']

class CriaForum(ModelForm):
    class Meta:
        model = Foruns
        fields = ['titulo', 'descricao']

