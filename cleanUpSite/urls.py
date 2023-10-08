"""cleanUp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inicial/', views.inicial, name='inicial'),
    path('create/', views.create, name='create'),
    path('sair', views.sair, name='sair'),
    path('sigin/', views.sigin, name='sigin'),
    path('criaF/', views.criaF, name='criaF'),
    path('desmatamento/', views.desmatamento, name="desmatamento"),
    path('lixao/', views.lixao),
    path('tema3/', views.tema3),
    path('forum/', views.forum, name='forum'),
    path('minhaConta/<int:pk>/', views.minhaConta, name='minhaConta'),
]

#path('criaForum/', views.criaForum, name='criaForum') -> apaguei essa rota