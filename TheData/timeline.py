import tweepy
import json
import os, sys
from textblob import TextBlob

# this program takes in multiple files of data that were created from our data crawler mtv.py and calculates the accumulated polarity of the tweets that were posted on each day. The output is then printed to the terminal.


def mean(numList):
	# returns average of a list of numbers

	return sum(numList)/len(numList)


if __name__=="__main__":

	count = 0
	days = {}
	polarity = {}
	num_files = int(sys.argv[1])
	#print num_files
	for i in range (1,num_files+1):
		input_file = open(sys.argv[1+i],'r')
		#print i
		for line in input_file:
			tweet_json = json.loads(line)
			tweet = TextBlob(tweet_json['text'])
			blob = TextBlob(tweet_json['created_at'])
			#print blob
			date = blob.split(' ')
			day = date[0]
			if day == 'Sun':
				day = "2016-04-03"
			if day == 'Mon':
				day = "2016-04-04"
			if day == 'Tue':
				day = "2016-04-05"
			if day == 'Wed':
				day = "2016-04-06"
			if day == 'Thu':
				day = "2016-04-07"
			if day == 'Fri':
				day = "2016-04-08"
			if day == 'Sat':
				day = "2016-04-09"
			if day not in days:
				days[day] = 1
				polarity[day] = [tweet.sentiment.polarity]
			if day in days:
				days[day] += 1
				polarity[day].append(tweet.sentiment.polarity)
			count += 1
	#print sorted(days.items())

	for key in polarity:
		polarity[key] = mean(polarity[key])
	for keys,values in sorted(days.items()):
		print keys, ": ", values, ", ", polarity[keys]
	print count

