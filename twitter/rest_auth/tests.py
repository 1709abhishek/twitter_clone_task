from django.contrib.auth.hashers import make_password
from django.test import TestCase, Client
import jwt
from rest_auth.models import TwitterUser, TwitterUserToken
from django.conf import settings


class TestAuthentication(TestCase):
    user = None

    def generate_token(self):
        payload = {
            'username': self.user.username,
            'email': self.user.email,
        }
        jwt_token = jwt.encode(payload, settings.ENCRYPTION_SECRET_KEY)
        TwitterUserToken.objects.create(token=jwt_token, user=self.user)

    def setUp(self):
        client = Client()
        self.user = TwitterUser.objects.create(email='', username='',
                                               password=make_password(''), contact_number='',
                                               first_name='', last_name='')
        self.generate_token()

    def check_login(self):
        response = self.client.post('/rest_auth/login/', {"username": "", "": ""})
        self.assertTrue(self.user.is_active)
        self.assertEquals(response.status_code, 200)

    def check_logout(self):
        response = self.client.get('/rest_auth/logout/',
                                   HTTP_AUTHORIZATION='TWEET {}'.format(self.user.user_token.token.decode()))
        self.assertEquals(response.status_code, 200)
