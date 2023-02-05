from django.test import TestCase
from .models import Task


class TestViews(TestCase):

    def test_get_login_page(self):
        response = self.client.get('/login/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/login.html')

    def test_get_register_page(self):
        response = self.client.get('/register/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/register.html')

    def test_get_create_page(self):
        response = self.client.get('/task-create/', follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertRedirects(response, '/login/?next=/task-create/')
