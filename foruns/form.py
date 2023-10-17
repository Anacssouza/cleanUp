from django.forms import ModelForm
from cleanUpSite.models import Foruns

class CriaForum(ModelForm):
    class Meta:
        model = Foruns
        fields = ['titulo', 'descricao']