import nltk
import spell_checker 
import math
class part_of_speech_extracter(object):
	""" Extract keywords from a list of tweets based on a configurable set of 
	parts of speech (only pick words that are a part of those parts of speech) """


	def __init__(self): 

		self.keywords = []
		self.popular_words_dictionary = {}
		self.spell_checker = spell_checker.spell_checker()
		self.populate_exceptions_dictionary()



	def parse_nouns_and_verbs(self, tweet_list): 
		""" For each tweet, pull out only the nouns and verbs in the tweet and 
		return a corresponding list 
			@param tweet_list: the list of input tweets 
			@return self.popular_words_dictionary: a dictionary with popular nouns and words with their frequencies 
		"""  

		tweet_list = [str(x) for x in tweet_list]
		for tweet in tweet_list: 
			tokens = nltk.word_tokenize(tweet)
			tagged = nltk.pos_tag(tokens)
			for word in tagged: 
				if word[1] =='NN' or word[1] == 'NNP' or word[1]== 'NNPS' or word[1] == 'VBD' or word[1] == 'VBN': 
					corrected_word = self.correct_word(word[0])
					cur_freq = self.popular_words_dictionary.get(corrected_word, 0)
					cur_freq += 1 
					self.popular_words_dictionary[corrected_word] = cur_freq
		return self.popular_words_dictionary


	def populate_exceptions_dictionary(self): 
		""" Populate a dictionary called exceptions_dictionary (a class attribute), with mappings of common mispellings to their 
		actual, correctly-spelled representations """ 

		self.exceptions_dictionary = {"u": "you", "ur": "your", "wen": "when", "y": "why"}


	def correct_word(self, word): 
		""" Given a word as input, determine if that word is a common mispelling, and if it is, return the word's mapping in the 
		exceptions dictionary. If the word is not a common mispelling, return the results of the spell_checker. If the word is not mispelled at all, 
		the function will simply return the word itself. 
			@param word: the word for which we want to determine the correct spelling 
		""" 

		new_word = word 
		if word in self.exceptions_dictionary.keys(): 
			new_word = self.exceptions_dictionary[word]
		else:
			new_word = self.spell_checker.correct(word)
		return new_word


class tf_idf(object): 
	""" Class that implements the TF-IDF (term frequency, inverse document frequency) algorithm """


	def __init__(self, corpora, keywords): 

		self.corpora = corpora # corpora is file of words
		self.keywords = keywords
		self.popular_words_dictionary = {}
		self.corpora_word_freq_dict = {}
		self.find_frequencies_of_words_in_corpora()


	def find_term_frequency(self, word, keywords): 
		""" 
		Find the term frequency of a word given: 
		@param word : a word we want the frequency of within a list or dict of keywords 
		@param keywords : a list or dict of keywords 
		"""

		if type(keywords) == dict: 
			return keywords[word]
		elif type(keywords) == list: 
			freq = 0 
			for each in keywords:
				if each == word: 
					freq +=1 
			return freq
		else: 
			return 0 

	def find_frequencies_of_words_in_corpora(self): 
		""" Finds the frequencies of each word in the class' corpora. Stores result in 
		corpora_word_freq_dict 
		"""

		for each in self.corpora: 
			cur_freq = self.corpora_word_freq_dict.get(each, 0)
			cur_freq += 0
			self.corpora_word_freq_dict[each] = cur_freq


	def tf_idf(self, word):
		""" 
		Main TF-IDF method 
			@param word: the word we want the weight for 
			@param term_frequency: the frequency of that word in the input 
			@param document_frequency: the frequency of the word in the document 

		""" 

		term_frequency = self.find_term_frequency(word, self.keywords)
		document_frequency = self.corpora_word_freq_dict[word]

		weight = float(term_frequency +1)/float(document_frequency +1)
		return math.log(weight)
