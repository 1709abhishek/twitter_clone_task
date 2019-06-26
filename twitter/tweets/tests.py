import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password

from rest_auth.models import TwitterUser, TwitterUserToken
from tweets.models import TweetFeed
from rest_framework.test import APIRequestFactory
from rest_framework.test import APITestCase
from tweets.views import  TweetFeeds


class TestTweets(APITestCase):
    user1 = None
    user2 = None
    tweet = None

    def generate_token(self):
        payload = {
            'username': self.user1.username,
            'email': self.user1.email,
        }
        jwt_token = jwt.encode(payload, settings.ENCRYPTION_SECRET_KEY)
        TwitterUserToken.objects.create(token=jwt_token, user=self.user1)

    def setUp(self):
        self.factory = APIRequestFactory()
        self.user1 = TwitterUser.objects.create(email='', username='',
                                                password=make_password(''), contact_number='',
                                                first_name='', last_name='')
        self.user2 = TwitterUser.objects.create(email='', username='',
                                                password=make_password(''), contact_number='',
                                                first_name='', last_name='')
        self.tweet = TweetFeed.objects.create(description='Test tweets', user=self.user1)
        self.generate_token()

    

    def test_post_tweet(self):
        request = self.factory.post('/tweets/tweet/', {'description': 'Testing creation of tweets'},
                                    HTTP_AUTHORIZATION='TWEET {}'.format(self.user1.user_token.token.decode()))
        request.user = self.user1
        view = TweetFeeds.as_view()
        response = view(request)
        self.assertTrue(response.status_code, 201)


