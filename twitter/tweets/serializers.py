import base64
import io

import magic
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from tweets.models import  TweetFeed, LikeTweetFeed




class TweetFeedsSerializer(serializers.ModelSerializer):
    



    def validate(self, attrs):
        if not attrs.get('description') or len(attrs.get('description')) > 500:
            msg = 'Invalid value'
            raise ValidationError(msg)
        return attrs

    def create(self, validated_data):
        description = validated_data.pop('description')
       
        user = self.context.get("user")
        tweet = TweetFeed.objects.create(description=description, user=user)
       

        return tweet

    class Meta:
        model = TweetFeed
        fields = ('tweet_id', 'description')


class LikeTweetSerializer(serializers.ModelSerializer):
    comment = serializers.CharField(max_length=500)

    def validate(self, attrs):
        if attrs.get('comment') and len(attrs.get('comment')) > 500:
            msg = 'Invalid value'
            raise ValidationError(msg)

        return attrs

    def create(self, validated_data):
        comment = validated_data.pop("comment", "")
        user = self.context.get("user")
        tweet = self.context.get("tweet")
        print(user, tweet)
        data = {
            "comment": comment,
            "user": user,
            "tweet": tweet
        }
        instance = LikeTweetFeed.objects.create(**data)
        return instance

    class Meta:
        model = LikeTweetFeed
        exclude = ('modified',)




