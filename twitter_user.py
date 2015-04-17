class twitter_user(object): 
	""" Class for a given user. Stores the twitter data object and 
	the username associated with a given user """ 

	def __init__(self, username): 
		self.username = None 
		self.twitter_data = None 


	def populate_twitter_data(self): 
		""" Populate the user object's twitter_data field with a populated twitter_data object """ 

		self.twitter_data = twitter_data(self.username)

