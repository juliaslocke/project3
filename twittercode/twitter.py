import tweepy

# Unique code from Twitter
access_token = "212628107-fn045K7WGY3zVbS9sDpnOJWuBKOs1opFqisYVg8O"
access_token_secret = "487ofYxbI0WodUgA2AZ2pGbxj8x8SXbYbvPNusF9nGMn6"
consumer_key = "VYGAxy53VirDKL8SLEI9MDZYM"
consumer_secret = "SjZghfbsOyAv3mcoccCvJ3URLCYcPy59FvtMWustiSeKVF5lrV"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('UMSI')


for tweet in public_tweets:
	print(tweet.text)
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

