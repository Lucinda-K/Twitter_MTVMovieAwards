CSE40437: Social Sensing and Cyber-Physical Systems
Final Project: Twitter_MTVMovieAwards
May 2nd, 2016
By: Emily Claps & Lucinda Krahl

The files necessary to run the data crawler and collect the data are in the folder 'DataCrawler.' The file 'mtv.py' is the program we used to collect data from Twitter using the Search API. In order to run the code, we hardcoded the beginning and end dates of the data collection as well as the keywords searched for. The beginning and end dates are hardcoded so that we were able to split up the collection of data from the first week to the second week and ensure that the data collection completed for each segment of time (when the rate limit is reached, the program sleeps for 15 minutes before continuing). The data is then stored in an output file that is labeled by the keyword as well as the beginning and end dates. Because our API keys are encrypted in the conf/settings.json file, be sure to create your own json config file with your API credentials or contact the authors.

Within 'TheData' folder, each of the category folders (BestActor, BestActress, BestKiss, and Movie_of_Year) contains the cumulative data of each of the nominees within their respective categories in the two weeks leading up to the awards on April 10th, 2016. Several of the scripts in TheData are also critical to be aware of in understanding our process of analyzing the data.

The file 'timeline.py' is a python script that takes as input the number of data files that are being analyzed followed by the names of the files themselves. It then outputs the average polarity of the tweets that were posted each day about the particular nominees being analyzed. For example, in order to find the polarity of the tweets for each day (in the two weeks leading up to the MTV awards) for Deadpool, type at the command line "python timeline.py 03-27:04-03_Deadpool.json 04-03:04-10_Deadpool.json.aa 04-03:04-10_Deadpool.json.ab 04-03:04-10_Deadpool.json.ac". The program will then output the average polarities of the tweets separated by the date on which they were posted. This allowed us to analyze the changes in the sentiment for each nominee over time. 

The program 'calculate.py' was extremely useful in analyzing the count and average polarity of the tweets from a data file while filtering out the retweets. We were able to run this program by using the command "python calculate.py" followed by the input file to be analyzed. Due to the fact that there were so many files that needed to be parsed through to filter retweets, we created the bash script 'textblob_plural.sh' that 

For example, in accumulating the average polarities and total number of tweets for all the files in the 'StraightOuttaCompton' folder, one would type in "./textblob_plural.sh Movie_of_Year/StraightOuttaCompton", and then the output is formatted as a 2-D array for each file in the folder - each line corresponding to a file. For example, 
[3646, 0.15020312784210474] 
[958, 0.24237037247090093]
indicates that the first file in the StraightOuttaCompton folder had 3646 tweets with an average polarity of 0.15, while the 2nd file had 958 tweets w/ an average polarity of 0.24. Because many of the folders have a large number of files, we copied this output and stored it in the text file "data.txt" which was then used as input in the script "parse_nonretweets.py". So, for example, in order to calculate the overall average polarity of our StraightOuttaCompton data, the above two lines would be copied to "data.txt" The command "python parse_nonretweets.py" would then be run and would output the following:
0.169381281698
4604.0
This indicates that the calculated average polarity for the film "Straight Outta Compton" was 0.169 & that there were a total of 4604 tweets. This process was repeated for each of the respective folders to gather the data for all the nominees.

