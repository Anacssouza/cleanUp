from django.forms import ModelForm
from cleanUpSite.models import Usuarios, Foruns

#class UsuariosForm(ModelForm):
#    class Meta:
#        model = Usuarios
#        fields = ['nome', 'email', 'senha']
#
#  estamos usando o módulo de autenticação do próprio django então não precisa mais disso aqui por enquanto
#  se for usar de novo tem que fazer as importações na views e descomentar tudo que tá lá
#  foi comentada nas configs a linha que colocava o módulo personalizado como o principal da autenticação
#  o arquivo da pasta backends ta inútil no momento com isso



class CriaForum(ModelForm):
    class Meta:
        model = Foruns
        fields = ['titulo', 'descricao']

