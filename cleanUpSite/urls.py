
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inicial/', views.inicial, name='inicial'),
    path('create/', views.create, name='create'),
    path('sair', views.sair, name='sair'),
    path('sigin/', views.login_site, name='login'),
    path('criaF/', views.criaF, name='criaF'),
    path('desmatamento/', views.desmatamento, name="desmatamento"),
    path('lixao/', views.lixao),
    path('tema3/', views.tema3),
    path('forum/', views.forum, name='forum'),
    path('minhaConta/', views.minhaConta, name='minhaConta'),
    path('editar/<str:username>', views.editar, name='editar'),
]

#path('criaForum/', views.criaForum, name='criaForum') -> apaguei essa rota