from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

class LoginSiteViewTest(TestCase):
    def setUp(self):
        # Criar um usuário de teste com credenciais válidas
        self.user = User.objects.create_user(username='testuser', password='testpassword1')

    def test_login_with_valid_credentials(self):
        # Faça uma solicitação POST para a view com as credenciais válidas configuradas em setUp
        response = self.client.post(reverse('desmatamento'), {
            'username': 'testuser',
            'senha': 'testpassword',
        })

        # Verifique se a resposta redireciona para a página minhaConta.html
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'desmatamento.html')

    def test_login_with_invalid_credentials(self):
        # Faça uma solicitação POST para a view com credenciais inválidas
        response = self.client.post(reverse('desmatamento'), {
            'username': 'invaliduser',
            'senha': 'invalidpassword',
        })

        # Verifique se a resposta permanece na página home.html e contém o erro
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'desmatamento.html')
      #  self.assertContains(response, 'Dados errados')



