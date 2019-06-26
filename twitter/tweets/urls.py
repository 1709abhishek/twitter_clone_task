from django.urls import path
from tweets.views import  TweetFeeds, UserTweetFeeds,LikeTweetView, \

urlpatterns = [
    path('tweet/', TweetFeeds.as_view()),
    path('tweet/<uuid:pk>/', TweetFeeds.as_view()),
    path('tweet/user/<uuid:pk>/', UserTweetFeeds.as_view()),
    path('tweet/like/<uuid:pk>/', LikeTweetView.as_view()),
]
