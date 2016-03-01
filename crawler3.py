# crawler3.py
# Description: Collects tweets with certain keywords and geotag
#
# Lucinda Krahl
# Assignment 1
# Tuesday, February 2, 2016


import tweepy	# for streaming tweets
import codecs	# for outputting ascii to .txt file properly

API_key = "wcskLByjo4Vic3ST5VjZtdert"
API_secret = "zYHNzEbnN5NFurALVxmS1NbbrXay54SQ03ciWdxpEEr9OB1Yqs"
access_token = "3247974236-PCsBe4ERedXGlxoM6m7nEMwY6MzTYgbzt56Ptvw"
access_token_secret = "pEL43CsaYPxVCORoxeIzEStN8oe2dXdSlxO2OehqPWWZ2"

auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

file = codecs.open("output3.txt", "w", "utf-8")

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

