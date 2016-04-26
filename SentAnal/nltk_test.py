from textblob.classifiers import NaiveBayesClassifier
from textblob import TextBlob

sentence = TextBlob("This is great!", "This sucks")

print sentence.sentiment
