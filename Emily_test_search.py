from __future__ import division

import tweepy	# for streaming tweets
import codecs	# for outputting ascii to .txt file properly

API_key = "V6SvjGRDb9cx9xjUYbk7cdWiv"
API_secret = "mbSTWuL7rxteJ8UFm3ygODqVfBPmKAu1vwXQoEVX0Q8qAva3yu"
access_token = "2991534147-2GZdjJypRYLHlOlYe8oP0HIDLX8zqqdVtFvl0Y0"
access_token_secret = "p43WYLmYfmt89uz9ivXZm2GIXxWOnicdabGLrsoPBRRYd"

auth = tweepy.OAuthHandler(API_key, API_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

api.search(q = 'hello', count=3, until='2016-02-25')
{u'search_metadata': {u'count': 3, u'completed_in': 0.007, u'max_id_str': u'9223372036854775807', u'since_id_str': u'0', u'refresh_url': u'?since_id=9223372036854775807&q=hello%20until%3A2012-01-01&include_entities=1', u'since_id': 0, u'query': u'hello+until%3A2012-01-01', u'max_id': 9223372036854775807L}, u'statuses': []}

file = codecs.open("results_Animated", "w", "utf-8")
#file = codecs.open("output3.txt", "w", "utf-8")

tweet_total = 0
first_tweet_time = "" 
last_tweet_time = ""

keyword = "\"Inside Out\""

queried_tweets = api.search(q = keyword)
#print queried_tweets
this = str(queried_tweets).split("text=u")
#for i in this:
#	print i + "\n\n"

tweet_total = len(this)
#print tweet_total

#for tweet in queried_tweets:
#	file.write(tweet)

#file.write("\n\n\nSUMMARY OF TWEETS\n\n\n")
#file.write("Number of tweets: %d\n\n" % tweet_total)
'''
file.write("First tweet",)
file.write(queried_tweets[0].created_at)
file.write("Last tweet",)
file.write(queried_tweets[tweet_total-1].created_at)
'''

#for tweet in queried_tweets:
#	file.write(tweet.text)
#	file.write("\n")

class MyStreamListener(tweepy.StreamListener):
	def __init__(self, api = None):
		super(MyStreamListener, self).__init__()
		self.num_tweets = 0

	def on_status(self,status):
		print(status.text)
		self.num_tweets += 1
		print str(self.num_tweets)

	def on_error(self, status_code):
		if status_code == 420:
			return False

auth = tweepy.OAuthHandler(API_key,API_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

WordStream = MyStreamListener()
myWordStream = tweepy.Stream(auth = api.auth, listener=WordStream)
myWordStream.filter(track=["Inside Out"], until= '2016-03-01', lang='en', async = True)
