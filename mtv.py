import tweepy	# for streaming tweets
import codecs	# for outputting ascii to .txt file properly
import json	# for parsing json
import sys,os
import csv
import time



consumer_key = "V6SvjGRDb9cx9xjUYbk7cdWiv"
consumer_secret = "mbSTWuL7rxteJ8UFm3ygODqVfBPmKAu1vwXQoEVX0Q8qAva3yu"
access_key = "2991534147-2GZdjJypRYLHlOlYe8oP0HIDLX8zqqdVtFvl0Y0"
access_secret = "p43WYLmYfmt89uz9ivXZm2GIXxWOnicdabGLrsoPBRRYd"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


class Query:

    def __init__(self):
        self.queried_tweets = 0

    def search_tweets(self, keyword, since_date, until_date):

        #limit = self.get_request_limit()
        #print limit
        tweet_count = 0
        keyword_str = keyword.replace(" ","_")
        keyword_str = keyword_str.strip("\"")
        outfile_str = since_date[-5:] + ":" + until_date[-5:] + "_" + keyword_str[:10] + ".txt"
        # create keywords string
        #keyword_str = "\"" + str(keywords).replace("_"," ") + "\""
        #since_date = since_date.replace("_"," ")
        #until_date = until_date.replace("_"," ")
        print "Search term: %s, Dates: %s to %s, Output: %s" % (keyword,since_date,until_date,outfile_str)

        out_file = None
        if not os.path.exists(outfile_str):
            out_file = codecs.open(outfile_str, "w", "utf8")
            out_file.close()

        out_file = codecs.open(outfile_str, "a", "utf8")

        cursor = tweepy.Cursor(api.search, q=keyword, count=100, lang='en', since=since_date, until=until_date, include_entities=True).items()
        while True:
            try:
                tweet = cursor.next()
                self.queried_tweets += 1
                try:
				json_str = json.dumps(tweet._json)
				out_file.write(str(json_str))
				out_file.write("\n")
				
                except Exception as e:
                    print 'exception is writing:', e.message
                    pass

            except tweepy.TweepError:
                print 'get tweep error, going to sleep'
                time.sleep(15 * 60)
                continue
            except StopIteration:
                print 'get stop iteration error'
                break
            except Exception as e:
                print 'any other exception:', e.message

        out_file.close()
        print "Found %i tweets",  str(self.queried_tweets)



if __name__=="__main__":

    since = '2016-04-03'
    until = '2016-04-09'

    keywords = ['"Star Wars: The Force Awakens" OR "Star Wars Episode VII" OR "Star Wars: Episode VII"']

    print keywords

    for keyword in keywords:
        myQuery = Query()
        myQuery.search_tweets(keyword,since,until)


