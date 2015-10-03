'''
twitterStream.py
Frederik Roenn Stensaeth
10.03.15

Python program that connects to Twitter and matches tweets that mention given
words. The sentiment of the matches is found and stored.

Credit given to PythonProgramming.net for the general idea of the program.
Credit given to text-processing.com for their sentiment api.
'''

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import urllib
import sys

# Fill these in manually.
# NOTE: Should make it such that these keys/secrets are loaded from separate
#		file automatically.
consumer_key = '' # Manually enter
consumer_secret = '' # Manually enter
access_token = '' # Manually enter
access_secret = '' # Manually enter

class streamer(StreamListener):
	
	def on_data(self, data):
		feed = json.loads(data)

		tweet = feed["text"]

		print(tweet)

		filtered_tweet = ''
		for character in tweet:
			# Need to make sure that text-processing.com is able to handle the
			# character. 
			if ord(character) <= 128:
				filtered_tweet += character

		# Testing
		print()
		print(filtered_tweet)
		print()

		# Connect up to text-processing.com -- they will handle the sentiment
		# analysis.
		# NOTE: This is probably a bottle-neck for the program, as it does not
		# 		run all too fast.
		# NOTE: Remember to look for a solution to this problem.
		payload = urllib.urlencode({"text": filtered_tweet}) 
		result = urllib.urlopen("http://text-processing.com/api/sentiment/", payload)
		# print result.read()
		# print result.info()

		content = json.load(result)

		print('Overall: ' + str(content['label']))

		# Test Start
		pos = content['probability']['pos']
		neg = content['probability']['neg']
		neu = content['probability']['neutral']

		print('Pos: ' + str(pos))
		print('Neg: ' + str(neg))
		print('Neu: ' + str(neu))

		print()
		# Test End

		# We only want to add the sentiment to our list, if it has some merit
		# to it.
        # NOTE: What if it is neutral? Check the difference between pos 
        #       and neg?
		if content['probability'][content['label']] >= 0.6:
			output = open('stream.txt', 'a')
			output.write(content['label'])
			output.write('\n')
			output.close()

		return True

	def on_error(self, status):
		print(status)

if len(sys.argv) != 2:
	print('Usage: $ python TwitterStream.py <word>')
	sys.exit()

authenication = OAuthHandler(consumer_key, consumer_secret)
authenication.set_access_token(access_token, access_secret)

twitter_stream = Stream(authenication, streamer())
twitter_stream.filter(track=[sys.argv[1]])





