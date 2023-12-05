import datetime

import pytz
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from django.utils import timezone

from cleanUpSite.models import Foruns, UserFor

class CriaForum(forms.Form):
    titulo = forms.CharField()
    descricao = forms.CharField(widget=forms.Textarea)


    def save(self, user):
        # Crie as instâncias dos modelos e preencha os campos
        novo_forum = Foruns(titulo=self.cleaned_data['titulo'], descricao=self.cleaned_data['descricao'])
        novo_forum.save()
        tz = pytz.timezone('America/Sao_Paulo')
        user_for = UserFor(user=user, data_participacao=timezone.now(), id_foruns_id=novo_forum.id_foruns)
        user_for.save()

# Em sua view
