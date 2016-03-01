


import tweepy	# for streaming tweets
import codecs	# for outputting ascii to .txt file properly
import json	# for parsing json

# Open config file, which contains API info 
with open("conf/settings.json") as json_file:
	info = json.load(json_file)
# load info from config dictionary
API_key = info["db"]["api_key"]
API_secret = info["db"]["api_secret"]
access_token = info["db"]["access_token"]
access_token_secret = info["db"]["access_token_secret"]

auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file = codecs.open("results_BrieLarson", "w", "utf-8")
#file = codecs.open("output3.txt", "w", "utf-8")

tweet_total = 0
first_tweet_time = ""
last_tweet_time = ""


keyword = "Brie Larson"



queried_tweets = api.search(q = keyword, count = 100)
tweet_total = len(queried_tweets)

for tweet in queried_tweets:
	file.write(tweet)

file.write("\n\n\nSUMMARY OF TWEETS\n\n\n")
file.write("Number of tweets: %d\n\n" % tweet_total)
'''
file.write("First tweet",)
file.write(queried_tweets[0].created_at)
file.write("Last tweet",)
file.write(queried_tweets[tweet_total-1].created_at)
'''

for tweet in queried_tweets:
	file.write(tweet.text)
	file.write("\n")

'''
# This uses a streaming API, as opposed to a search API, since the purpose is to collect real-time tweets.

# Create StreamListener class

class MyStreamListener(tweepy.StreamListener):

	def __init__(self, listener, api = None):
		self.listener = listener	# Name of stream
		self.api = tweepy.API(auth)
		self.tweet_count = 1		# Keep count of tweets
		self.max_tweets = 50		# Stop after 50 tweets

	def on_status(self, status):
		# print real-time tweets
		file.write("Stream: %s, Tweet: %d %s\n" % (self.listener, self.tweet_count, status.text))
		self.tweet_count += 1

		# close stream at max
		if self.tweet_count > self.max_tweets:
			return False

	def on_error(self, status_code):
	# deals with rate limits, disconnects stream
		if status_code == 420:
			file.write("Rate limit exceeded")
			return False

# Instantiate listener objects - open streams
myWordStream = tweepy.Stream(auth, listener=MyStreamListener('WeatherStream'))
myLocationStream = tweepy.Stream(auth, listener=MyStreamListener('LocationStream'))

file.write("Stream 1: Keywords \"weather\" OR \"indiana\"\n")
# Stream 1, keywords = "weather" and "indiana"
myWordStream.filter(track=['indiana','weather'], async=True)
file.write("\nStream 2: Location within South Bend\n")
# Stream 2, location = South Bend, IN (approximate)
myLocationStream.filter(locations=[-86.33,41.63,-86.20,41.74], async=True)
'''
