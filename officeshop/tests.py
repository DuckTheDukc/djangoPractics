from django.test import TestCase
from .forms import RegisterForm
from django.urls import reverse
from django.contrib.auth.models import User

class TestCaseViewAccount(TestCase):
    
    def setUp(self) -> None:
        self.form_data={
            'username':'ASDDFSG',
            'email': 'asdasdasd@gmail.com',
            'password1': 'Qwerty123456789_',
            'password2': 'Qwerty123456789_',
        }
    def test_register_view(self):
        
        RegisterForm(data=self.form_data)
        self.client.post(reverse('register'),data=self.form_data)
        user=User.objects.filter(username=self.form_data['username']).exists()
        self.assertTrue(user)
# Create your tests here.
