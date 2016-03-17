


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

		self.api = tweepy.API(auth)


class Query:

	def __init__(self,api):
		self.queried_tweets = []

	def search_tweets(self,keywords,since_date,until_date):

		# create keywords string
		keyword_str = "\"" + str(keywords) + "\""
		for tweet in tweepy.Cursor(api.search,q=keyword_str, count=100, lang='en').items():

			self.queried_tweets.append(tweet)


	def output_to_file(self,outfile):
#		print "Outputting to file..."
		print "Number of tweets: %d" % len(self.queried_tweets)
		outfile.write("id_str|created_at|text|retweeted\n")

		print queried_tweets[0]
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

if __name__=="__main__":

	if len(sys.argv) != 3:
		sys.exit('Usage: python program.py out_file search_term')

	output_file = str(sys.argv[1])
	search_term = str(sys.argv[2])

	file = codecs.open(output_file, "w", "utf-8")

	print "Creating api object..."
	myAPI = Tweepy_api()
	myAPI.setup_oauth()
	api = myAPI.api

	since = '2016-02-24'
	until = '2016-02-29'

	print "Creating Query object..."
	myQuery = Query(api)
	myQuery.search_tweets(search_term,since,until)

	print "Search term: %s, Dates: %s to %s, File: %s" % (search_term,since,until,output_file)

	myQuery.output_to_file(file)
#	myQuery.output_to_csv(file)
	file.close()

	sys.exit()

