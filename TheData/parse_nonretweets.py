#!/usr/bin/python


if __name__=="__main__":
	tot_count = 0
	tweet_count = []
	polarities = []

	f = open("data.txt",'r')
	for line in f:
		x = line.rstrip()
		x = x.split(', ')
		count = str(x[0]).replace('[','')
		tweet_count.append(int(count))
		tot_count += float(count)
		polarity = str(x[1]).replace(']','')
		polarities.append(float(polarity))
	f.close()
	print tweet_count
	print polarities
	
	sum = 0
	for i in range (0,len(tweet_count)):
		sum += float(tweet_count[i]) * float(polarities[i])
	print sum/tot_count
	print tot_count
