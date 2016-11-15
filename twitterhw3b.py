# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
#import pip
#pip.main(['install', 'textblob'])
from textblob import TextBlob

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

search_term = input('What would you like to search?')
public_tweets = api.search(search_term)


print('List of tweets: \n' )
subjectivity_score = 0
polarity_score = 0
for tweet in public_tweets:
	print(tweet.text + '\n')
	subjectivity_score += TextBlob(tweet.text).sentiment.subjectivity
	polarity_score += TextBlob(tweet.text).sentiment.polarity


avg_subjectivity = subjectivity_score / len(public_tweets)
avg_polarity = polarity_score / len(public_tweets)
print("Average subjectivity is %f" %avg_subjectivity)
print("Average polarity is %f" %avg_polarity)
