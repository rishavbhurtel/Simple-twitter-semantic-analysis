import tweepy
from textblob import TextBlob

consumer_key = 'hPD0bbNTStZttbVSwNiuNYMIF'
consumer_secret = '5yjKYtQh8jm3iq3umMwohuOCNkYRnhcS2wszRUghVLkvRpTK8l'

access_token = '242703630-zNoJo1h85s2EZ4cn1B6FsDCDr2n4YFa70MlhQPJk'
access_token_secret = 'mkQBD4qSABNcSu3H4utZ5plDWvXU7DHDex8fknwgAJ7pQ'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

