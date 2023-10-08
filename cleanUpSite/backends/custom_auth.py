from django.contrib.auth.backends import BaseBackend
from cleanUpSite.models import Usuarios

class EmailBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = Usuarios.objects.get(email=email, senha=password)
            return user
        except Usuarios.DoesNotExist:
            return None

# pra funcionar, em venv/Lib/django/contrib/auth no arquivo models.py comentei a linha -> def update_last_login(sender, user, **kwargs): pq tava pegando a data do ultimo login e tava bugando