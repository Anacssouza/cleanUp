
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('criaF/', views.criaF, name='criaF'),
    path('forum/', views.forum, name='forum'),
    path('excluiF/<int:pk>/', views.excluiF, name='excluiF'),
    path('editarF/<int:pk>/', views.editarF, name='editarF')

 #   path('minhaConta/', views.minhaConta, name='minhaConta'),
  #  path('editar/', views.editar, name='editar'),
   # path('deletarUsuario/<int:pk>/', views.deletarUsuario, name='deletarUsuario'),
]

#path('criaForum/', views.criaForum, name='criaForum') -> apaguei essa rota