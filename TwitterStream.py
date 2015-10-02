# Credit given to Python Programming dot net.

from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
import sentiment_mod as s

# Fill these in.
ckey = ''
csecret = ''
atoken = ''
asecret = ''

class listener(StreamListener):
	
	def on_data(self, data):
		all_data = json.loads(data)

		tweet = all_data["text"]

		print(tweet)

		sentiment_value, confidence = s.sentiment(tweet)

		if confidence * 100 >= 80:
			output = open('Twitter-out.txt', 'a')
			output.write(sentiment_value)
			output.write('\n')
			output.close()

		return True

	def on_error(self, status):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitter_stream = Stream(auth, listener())
twitter_stream.filter(tack=['Trump'])