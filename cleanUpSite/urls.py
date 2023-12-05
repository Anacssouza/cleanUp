
from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views



handler404 = 'cleanUpSite.views.custom_404_page'
handler500 = 'cleanUpSite.views.custom_500_page'

urlpatterns = [
    path('', views.desmatamento, name='home'),
    path('create/', views.create, name='create'),
    path('sair', views.sair, name='sair'),
    path('sigin/', views.login_site, name='login'),
    path('desmatamento/', views.desmatamento, name="desmatamento"),
    path('minhaConta/', views.minhaConta, name='minhaConta'),
    path('editar/', views.editar, name='editar'),
    path('deletarUsuario/<int:pk>/', views.deletarUsuario, name='deletarUsuario'),
    path('editar/alterar_senha/', views.alterar_senha, name='alterar_senha'),
    path('contato/', views.contato, name='contato'),
    path('teste404/', views.teste404, name='teste404'),
    path('teste500/', views.teste500, name='teste500'),
    path('enviaemail/', views.enviaemail, name='enviaemail'),
    path('conteudos/', views.conteudos, name='conteudos'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='recuperarSenha/password-reset.html'), name="password_reset"),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='recuperarSenha/password-reset-done.html'), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='recuperarSenha/password-reset-confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='recuperarSenha/password-reset-complete.html'), name='password_reset_complete'),





]

#path('criaForum/', views.criaForum, name='criaForum') -> apaguei essa rota

