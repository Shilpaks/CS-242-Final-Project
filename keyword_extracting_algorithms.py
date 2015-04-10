import nltk

class part_of_speech_extracter(object):
	""" Extract keywords from a list of tweets based on a configurable set of 
	parts of speech (only pick words that are a part of those parts of speech) """

	def __init__(self): 
		self.keywords = []
		self.popular_words_dictionary = {}

	def parse_nouns_and_verbs(self, tweet_list): 
		""" For each tweet, pull out only the nouns and verbs in the tweet and 
		return a corresponding list """  

		tweet_list = [str(x) for x in tweet_list]
		for tweet in tweet_list: 
			tokens = nltk.word_tokenize(tweet)
			tagged = nltk.pos_tag(tokens)
			for word in tagged: 
				if word[1] =='NN' or word[1] == 'NNP' or word[1]== 'NNPS' or word[1] == 'VBD' or word[1] == 'VBN': #tags are just nouns for the time being
					cur_freq = self.popular_words_dictionary.get(word[0], 0)
					cur_freq += 1 
					self.popular_words_dictionary[word[0]] = cur_freq
		return self.popular_words_dictionary

class tf_idf(object): 
	""" Class that implements the TF-IDF (term frequency, inverse document frequency) algorithm """

	def __init__(self): 
		self.corpora 
		self.keywords = []
		self.popular_words_dictionary = {}
		self.corpora_word_freq_dict 

	def tf_idf(self, word, frequency):
		""" Main TF-IDF method """ 
		pass



	def find_frequencies_of_words_in_corpora(self): 
		""" Finds the frequencies of each word in the class' corpora. Stores result in 
		corpora_word_freq_dict """
		# corpora is a list of words
		for each in self.corpora: 
			cur_freq = self.corpora_word_freq_dict.get(each, 0)
			cur_freq += 0
			self.corpora_word_freq_dict[each] = cur_freq

