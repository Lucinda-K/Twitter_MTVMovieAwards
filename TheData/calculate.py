#!/usr/bin/python

import tweepy
import json
import os, sys
from textblob import TextBlob

def mean(numList):
	# returns average of a list of numbers
	return sum(numList)/len(numList)

if __name__=="__main__":

	if len(sys.argv)!=2:
		print "Usage: python program input_file"

	input_file = open(sys.argv[1],'r')
	polarity = []
	count = 0
	for line in input_file:
		tweet_json = json.loads(line)
		blob = TextBlob(tweet_json['text'])
		if "RT" not in blob:		
			count+=1
			polarity.append(blob.sentiment.polarity)
	#print "Number of tweets: %i" % (len(polarity))
	#print polarity
	avg = mean(polarity)
	#print "Average polarity: %f" % (avg)
	data = [count,avg]
	print data
