import tweepy

CONSUMER_KEY = "V6SvjGRDb9cx9xjUYbk7cdWiv"
CONSUMER_SECRET = "mbSTWuL7rxteJ8UFm3ygODqVfBPmKAu1vwXQoEVX0Q8qAva3yu"
ACCESS_KEY = "2991534147-2GZdjJypRYLHlOlYe8oP0HIDLX8zqqdVtFvl0Y0"
ACCESS_SECRET = "p43WYLmYfmt89uz9ivXZm2GIXxWOnicdabGLrsoPBRRYd"

class MyStreamListener(tweepy.StreamListener):
	def __init__(self, api = None):
		super(MyStreamListener, self).__init__()
		self.num_tweets = 0

	def on_status(self,status):
		print(status.text)
		self.num_tweets += 1
		print str(self.num_tweets)
		
		if self.num_tweets == 50:
			exit()

	def on_error(self, status_code):
		if status_code == 420:
			return False

auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)

WordStream = MyStreamListener()
myWordStream = tweepy.Stream(auth = api.auth, listener=WordStream)
myWordStream.filter(track=['weather','Indiana'], async = True)

LocationStream = MyStreamListener()
myLocationStream = tweepy.Stream(auth = api.auth, listener=LocationStream)
myLocationStream.filter(locations=[-86.33,41.63,-86.20,41.74], async = True)

