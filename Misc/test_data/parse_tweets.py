# This program parses through the input of Oscar data! (collected for movie Spotlight)
# 100 tweets total

with open("Spotlight3.txt") as spotlightdata:
	content = spotlightdata.readlines()

for i in content:
	tweet = i.split('|')
	print tweet[1] + '\n'

'''
words = data.split('|')
print words

for i in range(0,len(words)):
	print words[i]
	print "\n"
'''

