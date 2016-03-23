


import tweepy	# for streaming tweets
import codecs	# for outputting ascii to .txt file properly
import json	# for parsing json
import sys,os
import csv

class Tweepy_api:

	def __init__(self):

		self.api_key = ""
		self.api_secret = ""
		self.access_token = ""
		self.access_token_secret = ""
		self.api = None

	def get_credentials(self):

		# Open config file, which contains API info 
		with open("conf/settings.json") as json_file:
			info = json.load(json_file)
		# load info from config dictionary
		self.api_key = info["lk"]["api_key"]
		self.api_secret = info["lk"]["api_secret"]
		self.access_token = info["lk"]["access_token"]
		self.access_token_secret = info["lk"]["access_token_secret"]
	
	def setup_oauth(self):
		self.get_credentials()
		auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)

		self.api = tweepy.API(auth, retry_count=3, retry_delay=5, retry_errors=set([401,404,500,503]), wait_on_rate_limit=True)


	def on_error(self, status_code):
	# deals with rate limits, disconnects stream
		if status_code == 420:
			print "Rate limit exceeded"
			return False

class Query:

	def __init__(self,api):
		self.queried_tweets = []
		self.api = api

	def search_tweets(self,keywords,since_date,until_date,outfile):
#	def search_tweets(self,keywords):

		tweet_count = 0
		# create keywords string
		keyword_str = "\"" + str(keywords).replace("_"," ") + "\""
		print "Search term: %s, Dates: %s to %s" % (keyword_str,since_date,until_date)

		for tweet in tweepy.Cursor(api.search,q=keyword_str, count=100, lang='en').items():
			#print tweet
			json_str = json.dumps(tweet._json)
			#print json_str
			#json_str = json.dumps(tweet)
			outfile.write(str(json_str))
			outfile.write("\n")
			self.queried_tweets.append(tweet)
			tweet_count+=1
			if tweet_count%100 == 0:
				print "Tweet %i: %s" % (tweet_count, tweet.created_at)

		
		print "Found %i tweets" % len(self.queried_tweets)

	def output_to_file(self,outfile):
#		print "Outputting to file..."
		print "Number of tweets: %d" % len(self.queried_tweets)
		outfile.write("id_str|created_at|text|retweeted\n")

		for tweet in self.queried_tweets:

			outfile.write(tweet.id_str)
			outfile.write("|")
			outfile.write(str(tweet.created_at))
			outfile.write("|")
			outfile.write(tweet.text.replace("|",";"))
			outfile.write("|")
			outfile.write(str(tweet.retweeted))
			outfile.write("\n")


	def output_to_csv(self,csvfile):
		
		csv_tweets = [[tweet.id_str.encode("utf-8"), str(tweet.created_at).encode("utf-8"), tweet.text.encode("utf-8"), str(tweet.retweeted).encode("utf-8")] for tweet in self.queried_tweets]

		writer = csv.writer(csvfile)
		writer.writerow(["id","created_at","text","retweeted"])
		writer.writerows(csv_tweets)

	def on_error(self, status_code):
	# deals with rate limits, disconnects stream
		if status_code == 420:
			file.write("Rate limit exceeded")
			return False

if __name__=="__main__":

	if len(sys.argv) != 5:
		sys.exit('Usage: python program.py out_file search_term since until --> Date format:yyyy-mm-dd')

	output_file = str(sys.argv[1])
	search_term = str(sys.argv[2])
	since = str(sys.argv[3])
	until = str(sys.argv[4])

	file = codecs.open(output_file, "w", "utf8")

	print "Creating api object..."
	myAPI = Tweepy_api()
	myAPI.setup_oauth()
	api = myAPI.api

	print "Creating Query object..."
	myQuery = Query(api)
	myQuery.search_tweets(search_term,since,until,file)
#	myQuery.search_tweets(search_term)

#	print "Search term: %s, Dates: %s to %s, File: %s" % (search_term,since,until,output_file)

	#myQuery.output_to_file(file)
#	myQuery.output_to_csv(file)
	file.close()

	sys.exit()

