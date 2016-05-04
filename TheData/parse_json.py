import sys
import json
# This program outputs the count of the number of tweets in a json file!

if __name__=="__main__":
		
	if len(sys.argv)!=2:
		print "Usage: python program input_file"
		sys.exit()

	input_file = sys.argv[1]

	with open(input_file) as f:
		lines = []
		tweet_count = 0
		for line in f:
				#print "NEW - %s" % line[:10]
			# new tweet, starts with id
			tweet = json.loads(line)
			lines.append(tweet)
			#print tweet['id']
			tweet_count+=1
		
	print "File contains " + str(tweet_count) + " tweets."
