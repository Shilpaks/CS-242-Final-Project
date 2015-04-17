import credentials
import keyword_extracting_algorithms 
import tweepy
import spell_checker
import nltk

class twitter_data(object): 
	""" Twitter data class -- responsible for authentication, storing keywords, and is tied to a 
	user object """ 

	def __init__(self, username): 

		self.username = username
		self.tweet_list = []
		self.keyword_list = []
		self.popular_words_dictionary = {}


	def authentication(self): 
		""" OAuth Authentication for Twitter API """ 

		consumer_key = credentials.twitter_consumer_key
		consumer_secret = credentials.twitter_consumer_secret
		access_token = credentials.twitter_access_token
		access_token_secret = credentials.twitter_access_token_secret
		auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
		auth.set_access_token(access_token, access_token_secret)
		auth.secure = True
		api = tweepy.API(auth)

		return api 


	def get_tweets(self, api): 
		""" Get a user's most recent tweets
		@param api : the api object returned by the authentication method 
		@return list of tweets 
		 """ 

		pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()
		user = api.get_user(self.username)
		public_tweets = api.home_timeline()
		my_tweets = []
		for tweet in public_tweets:
			my_tweets.append(tweet.text)

		return [str(x) for x in my_tweets]



	def twitter_data_wrapper(self): 
		""" Wrapper for authentication and tweet extraction """ 

		api = self.authentication()
		my_tweets = self.get_tweets(api)
		return my_tweets


		

def main(): 
	td = twitter_data('testuser242')
	api = td.authentication()
	print td.twitter_data_wrapper()




if __name__ == '__main__':
  	main()
