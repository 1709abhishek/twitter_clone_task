from django.db import models
from model_utils.models import TimeStampedModel
import uuid
from rest_auth.models import TwitterUser


class TweetFeed(TimeStampedModel):
    tweet_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    description = models.TextField()
    user = models.ForeignKey(TwitterUser, related_name='tweets', on_delete=models.CASCADE, null=True)
    liked_by = models.ManyToManyField(TwitterUser, related_name='liked_tweets', null=True)
    retweeted_by = models.ManyToManyField(TwitterUser, related_name='retweeted_tweets', null=True,
                                          through='ReTweetFeed')

class LikeTweetFeed(TimeStampedModel):
    Liketweet_id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    tweet = models.ForeignKey(TweetFeed, on_delete=models.CASCADE, related_name='retweets', null=True)
    user = models.ForeignKey(TwitterUser, on_delete=models.CASCADE, related_name='retweets', null=True)
    comment = models.TextField(null=True)



