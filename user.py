class user(object):

	""" Represention of a user within the system """ 

	def __init__ (self, twitter_username, phone_number): 
		self.twitter_username = twitter_username 
		self.phone_number = phone_number

	def get_twitter_username(self): 
		""" Getter Convenience method """
		return self.twitter_username
	def get_phone_number(self): 
		""" Getter convenience method """ 
		return self.phone_number

