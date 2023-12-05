
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

    path('criaF/', views.criaF, name='criaF'),
    path('forum/', views.forum, name='forum'),
    path('excluiF/<int:pk>/', views.excluiF, name='excluiF'),
    path('editarF/<int:pk>/', views.editarF, name='editarF')


]

