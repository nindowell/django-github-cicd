from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your tests here.


class CustomUserTests(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='12345'
        )

    def test_login_view(self):
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/login.html')

        data = {
            'username': 'testuser',
            'password': '12345'
        }
        response = self.client.post(reverse('users:login'), data)
        self.assertEqual(response.status_code, 302)  # redirect again
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_signup_view(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/signup.html')

        data = {
            'username': 'newuser',
            'email': 'newuser@example.com',
            'password1': 'newpass123',
            'password2': 'newpass123'
        }
        response = self.client.post(reverse('users:signup'), data)
        self.assertEqual(response.status_code, 302)  # should redirect to login?
        self.assertTrue(get_user_model().objects.filter(username='newuser').exists())

    def test_profile_view(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(reverse('users:profile'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'users/profile.html')
