from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=6)

class Publicacoes(models.Model):
    id_publi = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    data = models.DateTimeField()
#    forunz = models.ForeignKey('Foruns', on_delete=models.CASCADE, related_name='publicacoes_foruns')
#    admin = models.ForeignKey('ADM', on_delete=models.CASCADE, related_name='publicacoes_admin')

class Ecossistema(models.Model):
    id_eco = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=50)

class ProblemaAmbiental(models.Model):
    id_problema_amb = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=255)

class Instituicao(models.Model):
    nome = models.CharField(max_length=50)
    id_instituicao = models.AutoField(primary_key=True)
    endereco = models.CharField(max_length=100)
    email = models.EmailField(max_length=50)

class Projeto(models.Model):
    id_projeto = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    descricao = models.CharField(max_length=200)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    id_instituicao = models.ForeignKey(Instituicao, on_delete=models.CASCADE)

class ADM(models.Model):
    id_adm = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    senha = models.CharField(max_length=6)

class Foruns(models.Model):
    id_foruns = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=50)
    descricao = models.CharField(max_length=1000)

class UserFor(models.Model):
    id_foruns = models.ForeignKey(Foruns, on_delete=models.CASCADE)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_userfor = models.AutoField(primary_key=True)
    data_participacao = models.DateTimeField()

class UserPubli(models.Model):
    id_userpubli = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    id_publi = models.ForeignKey(Publicacoes, on_delete=models.CASCADE)
    data_interacao = models.DateTimeField()

# Adicionando chaves estrangeiras para Publicacoes
Publicacoes.add_to_class('id_foruns', models.ForeignKey(Foruns, on_delete=models.CASCADE))
Publicacoes.add_to_class('id_adm', models.ForeignKey(ADM, on_delete=models.CASCADE))