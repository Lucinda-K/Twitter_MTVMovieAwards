

import tweepy	# for streaming tweets
import codecs	# for outputting ascii to .txt file properly
import json	# for parsing json
import sys,os
import csv
import time

def mean(numList):
	# returns average of a list of numbers

	return sum(numList)/len(numList)


if __name__=="__main__":

	# input: our tweet txt file;
		# format: id|created_at|text|RT
	# output: json (aka dictionary) of the tweets

	if len(sys.argv)!=2:
		print "Usage: python program input_file"
		sys.exit()


	input_file = sys.argv[1]
	#lines = []

	with open(input_file) as f:
		lines = []
		tweet_count = 0
		line_count = 0
		for line in f:
			if line[:10].isdigit():
				#print "NEW - %s" % line[:10]
			# new tweet, starts with id
				lines.append(line.strip("\n"))
				tweet_count+=1
			else:
			# continuation of tweet from line before
				#print "SAME - %s" % line[:10]
				lines[len(lines)-1] = lines[len(lines)-1]+ " " + line.strip("\n")
				
			line_count+=1
	print("Lines: %i\nTweets:%i") % (line_count,tweet_count)
	

	outfile_str = input_file[:-3] + "json"
	print "Output file: %s" % outfile_str
	file = codecs.open(outfile_str, "w", "utf8")




	for line in lines:
		tweet = {}
		# Add to dictionary
		values = line.split("|")
		#print values
		if values[1]!='False':
		# not a nulle tweet
			tweet['id'] = values[0]
			tweet['created_at'] = values[1]
			tweet['text'] = values[2]
			#print tweet
			# dump as json and output
			json.dump(tweet,file)
			file.write("\n")
			# clear dictionary for next tweet
			tweet.clear()
		
'''
		json = json.dumps(tweet.decode('utf8'))
		file.write(json)
		file.write("\n")

		tweet.clear()		

	for line in lines:
		file.write(line.decode('utf8'))
		file.write("\n")
'''
