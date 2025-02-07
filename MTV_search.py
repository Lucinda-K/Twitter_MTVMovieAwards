


import tweepy	# for streaming tweets
import codecs	# for outputting ascii to .txt file properly
import json	# for parsing json
import sys,os
import csv
import time

class Tweepy_api:

	def __init__(self):

		self.api_array = ["lk","ec","ad"]
		self.api_user = 0
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
		self.api_key = info[self.api_array[self.api_user]]["api_key"]
		self.api_secret = info[self.api_array[self.api_user]]["api_secret"]
		self.access_token = info[self.api_array[self.api_user]]["access_token"]
		self.access_token_secret = info[self.api_array[self.api_user]]["access_token_secret"]
	
	def setup_oauth(self):
		self.get_credentials()
		auth = tweepy.OAuthHandler(self.api_key, self.api_secret)
		auth.set_access_token(self.access_token, self.access_token_secret)

		self.api = tweepy.API(auth, retry_count=3, retry_delay=5, retry_errors=set([401,404,500,503]))


	def on_error(self, status_code):
	# deals with rate limits, disconnects stream
		if status_code == 420:
			print "Rate limit exceeded"
			return False
	
	def switch_api(self):
		if self.api_user < 2:
			self.api_user+=1
		if self.api_user == 2:
			self.api_user = 0		

class Query:

	def __init__(self,api,api_obj):
		self.queried_tweets = []
		self.api = api
		self.API_obj = api_obj

	def get_request_limit(self):
		data = self.api.rate_limit_status()
		requests_remaining = data['resources']['search']['/search/tweets']['remaining']
		return requests_remaining

	def search_tweets(self,keywords,since_date,until_date):

		limit = self.get_request_limit()
		print limit
		tweet_count = 0
		keyword_str = keywords.replace(" ","_")
		keyword_str = keyword_str.strip("\"")
		outfile_str = since_date[-5:] + ":"+ until_date[-5:] + "_" + keyword_str[:10] + ".txt"
		# create keywords string
		#keyword_str = "\"" + str(keywords).replace("_"," ") + "\""
		#since_date = since_date.replace("_"," ")
		#until_date = until_date.replace("_"," ")
		print "Search term: %s, Dates: %s to %s, Output: %s" % (keywords,since_date,until_date,outfile_str)

		file = codecs.open(outfile_str, "w", "utf8")

		for tweet in tweepy.Cursor(api.search,q=keywords, count=100, lang='en',since=since_date,until=until_date).items():

			try:
				#print tweet
				json_str = json.dumps(tweet._json)
				#print json_str
				#json_str = json.dumps(tweet)
				file.write(str(json_str))
				file.write("\n")
				self.queried_tweets.append(tweet)
				tweet_count+=1

				#data = self.x-rate-remaining()
				#data_dump = json.dumps(self.api.rate_limit_status())
				
				if tweet_count%1000 == 0:
					print "Tweet %i: %s" % (tweet_count, tweet.created_at)
					print "Requests remaining: %i" % self.get_request_limit()
					
			except Exception as e:
				print e.message[0]['code']
				print e.args[0][0]['code']
				#if status_code == 429:
					#print e.response.status
				if "limit" in str(e.message) or "exceeded" in str(e.message):
					print "going to sleep for 15 minutes, current counter:", counter, time.time()
					time.sleep(15 * 60)
				API_obj.switch_api()
				print "switching api user!!"

		
		print "Found %i tweets" % len(self.queried_tweets)

		file.close()

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

	if len(sys.argv) != 4:
		sys.exit('Usage: python program.py input_file since_date until_date --> Date format: yyyy-mm-dd')
	# GET INPUT FILE INFO

	input_file = open(sys.argv[1],'r')
	since = str(sys.argv[2])
	until = str(sys.argv[3])

	keywords = []
	for line in input_file:

		line = line.strip("\n")
		keywords.append(line)
		
		#search

#	output_file = str(sys.argv[1])
#	search_term = str(sys.argv[2])
#	since = str(sys.argv[3])
#	until = str(sys.argv[4])


#	file = codecs.open(output_file, "w", "utf8")

	print "Creating api object..."
	myAPI = Tweepy_api()
	myAPI.setup_oauth()
	api = myAPI.api
	api_user = myAPI.api_user
	print "API User: ", api_user

	print "Creating Query object..."

	for keyword in keywords:
		myQuery = Query(api,myAPI)
		myQuery.search_tweets(keyword,since,until)
#	myQuery.search_tweets(search_term)

#	print "Search term: %s, Dates: %s to %s, File: %s" % (search_term,since,until,output_file)

	#myQuery.output_to_file(file)
#	myQuery.output_to_csv(file)
	#file.close()

	sys.exit()

