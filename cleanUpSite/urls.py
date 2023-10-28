
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inicial/', views.inicial, name='inicial'),
    path('create/', views.create, name='create'),
    path('sair', views.sair, name='sair'),
    path('sigin/', views.login_site, name='login'),
    path('desmatamento/', views.desmatamento, name="desmatamento"),
    path('lixao/', views.lixao),
    path('tema3/', views.tema3),
    path('minhaConta/', views.minhaConta, name='minhaConta'),
    path('editar/', views.editar, name='editar'),
    path('deletarUsuario/<int:pk>/', views.deletarUsuario, name='deletarUsuario'),
    path('foto/', views.upload_profile_picture, name='upload_profile_picture'),

]

#path('criaForum/', views.criaForum, name='criaForum') -> apaguei essa rota