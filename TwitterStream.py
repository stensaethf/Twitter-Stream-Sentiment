# Credit given to Python Programming dot net.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import urllib
# import sentiment_mod as s

# Fill these in.
ckey = '' # Manually enter
csecret = '' # Manually enter
atoken = '' # Manually enter
asecret = '' # Manually enter

class listener(StreamListener):
	
	def on_data(self, data):
		all_data = json.loads(data)

		tweet = all_data["text"]

		print(tweet)

		filtered_tweet = ''
		for i in tweet:
			if ord(i) <= 128:
				filtered_tweet += i
			# For testing.
			# else:
			# 	print(ord(i))

		# Testing
		print()
		print(filtered_tweet)
		print()

		# Connect up to text-processing.com -- they will handle the sentiment
		# analysis.
		payload = urllib.urlencode({"text": filtered_tweet}) 
		result = urllib.urlopen("http://text-processing.com/api/sentiment/", payload)
		# print result.read()
		# print result.info()

		content = json.load(result)

		print('Overall: ' + str(content['label']))

		pos = content['probability']['pos']
		neg = content['probability']['neg']
		neu = content['probability']['neutral']

		print('Pos: ' + str(pos))
		print('Neg: ' + str(neg))
		print('Neu: ' + str(neu))

		print()

		# if confidence * 100 >= 80:
		# 	output = open('Twitter-out.txt', 'a')
		# 	output.write(sentiment_value)
		# 	output.write('\n')
		# 	output.close()

		return True

	def on_error(self, status):
		print(status)

oauth = OAuthHandler(ckey, csecret)
oauth.set_access_token(atoken, asecret)

twitter_stream = Stream(oauth, listener())
twitter_stream.filter(track=['Trump'])





