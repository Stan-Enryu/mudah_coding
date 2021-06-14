from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User


class BaseTest(TestCase):
    def priori(self):
        self.reg_url = reverse('register')
        self.login_url = reverse('login')
        self.user = {
            'username':'stanleyganteng',
            'email':'stan@gmail.com',
            'password':'binexgampangbanget1337',
            'password2':'binexgampangbanget1337'
        }
        #{'username':'stanleyganteng', 'email':'stan@gmail.com', 'password':'binexgampangbanget1337', 'password2':'binexgampangbanget1337'} 
        self.user_gagal_konfirmasi_password = {
            'username':'stanleyganteng',
            'email':'stan@gmail.com',
            'password':'binexgampangbanget1337',
            'password2':'binekezbangetttttt1337'
        }
        #{'username':'stanleyganteng', 'email':'stan@gmail.com', 'password':'binexgampangbanget1337', 'password2':'binekezbangetttttt1337'} 
        self.user_passwordnya_kependekan = {
            'username':'stanleyganteng',
            'email':'stan@gmail.com',
            'password':'ha',
            'password2':'ha'
        }
        #{'username':'stanleyganteng', 'email':'stan@gmail.com', 'password':'ha', 'password2':'ha'} 
        self.user_emailnya_ga_valid = {
            'username':'stanleyganteng',
            'email':'inibukanemailya',
            'password':'haiyahaiya1337',
            'password2':'haiyahaiya1337'
        }
        #{'username':'stanleyganteng', 'email':'inibukanemailya', 'password':'haiyahaiya1337', 'password2':'haiyahaiya1337'} 
        return super().priori()

class RegisterTesting(BaseTest):
    def register_site_nya_bisa_dikunjungi(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/register.html')

    def user_registration_validation(self):
        response = self.client.post(reverse('register'),{'username':'stanleyganteng', 'email':'stan@gmail.com', 'password':'binexgampangbanget1337', 'password2':'binexgampangbanget1337'},format='text/html')
        self.assertEqual(response.status_code,200)

    def short_password_testing_registration(self):
        response = self.client.post(reverse('register'),{'username':'stanleyganteng', 'email':'stan@gmail.com', 'password':'ha', 'password2':'ha'},format='text/html')
        self.assertEqual(response.status_code,200)

    def passwordconfirmation_registernya_salah(self):
        response = self.client.post(reverse('register'),{'username':'stanleyganteng', 'email':'stan@gmail.com', 'password':'binexgampangbanget1337', 'password2':'binekezbangetttttt1337'},format='text/html')
        self.assertEqual(response.status_code,200)

    def user_email_registrasinya_salah(self):
        response = self.client.post(reverse('register'),{'username':'stanleyganteng', 'email':'inibukanemailya', 'password':'haiyahaiya1337', 'password2':'haiyahaiya1337'},format='text/html')
        self.assertEqual(response.status_code,200)

class LoginTesting(BaseTest):
    def akses_page_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'users/login.html')

    def test_login_valid(self):
        self.client.post(reverse('register'),{'username':'stanleyganteng', 'email':'stan@gmail.com', 'password':'binexgampangbanget1337', 'password2':'binexgampangbanget1337'},format='text/html')
        response = self.client.post(reverse('login'),{'username':'stanleyganteng','password':'binexgampangbanget1337'},format='text/html')
        self.assertEqual(response.status_code,200)

    def ga_bisa_login_tanpa_username(self):
        response = self.client.post(reverse('login'),{'password':'anjaymarinjay123','username':''},format='text/html')
        self.assertEqual(response.status_code,200)

    def ga_bisa_login_tanpa_password(self):
        response = self.client.post(reverse('login'),{'username':'stanleyganteng','password':''},format='text/html')
        self.assertEqual(response.status_code,200)