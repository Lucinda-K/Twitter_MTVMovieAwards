#!/usr/bin/python


if __name__=="__main__":
	tot_count = 0
	tweet_count = []
	polarities = []

	f = open("creed.txt",'r')
	for line in f:
		if 'polarity' in line:
			x = line.split(": ")
			polarities.append(x[1].rstrip())
		if 'tweets' in line:
			x = line.split(": ")
			tweet_count.append(x[1].rstrip())
			tot_count += int(x[1])
	f.close()
	
	sum = 0
	for i in range (0,len(tweet_count)):
		sum += float(tweet_count[i]) * float(polarities[i])
	print sum/tot_count
	print tot_count
