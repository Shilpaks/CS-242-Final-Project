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
					corrected_word = word[0] #self.correct_word(word[0])
					cur_freq = self.popular_words_dictionary.get(corrected_word, 0)
					cur_freq += 1 
					self.popular_words_dictionary[corrected_word] = cur_freq
		return self.popular_words_dictionary

	def lemmatization(self, word):
		""" Function that implements lemmatization. Lemmatization is grouping words of the same meaning or base morpheme together
			@param word: The word to be lemmatized 
		""" 

		lemmatizer = nltk.WordNetLemmatizer()
		lemmatized_word = lemmatizer.lemmatize(word)
		return lemmatized_word

	def lemmatization_with_correction(self, word):
		""" Function that implements lemmatization. Lemmatization is grouping words of the same meaning or base morpheme together WITH correction. 
			Double checks that stem is actually a word.
			@param word: The word to be lemmatized 
		""" 

		lemmatizer = nltk.WordNetLemmatizer()
		lemmatized_word = lemmatizer.lemmatize(word)
		if self.check_if_lemmatized_word_is_real(word, lemmatized_word): 
			return lemmatized_word
		else:
			return word 

	def check_if_lemmatized_word_is_real(self, old_word, new_word): 
		""" Check if a word that has been lemmatized is still a word that exists in the dictionary """

		new_word_corrected = self.correct_word(new_word)
		if new_word_corrected != old_word: 
			return False 
		else: 
			return True 

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

class stemmer(object): 
	""" Class that implements stemming in the context of lemmatization """
	def __init__(self, word_freq_dict): 
		""" Morphological constants or inflectional morphemes """ 
		self.morphemes = ["ed", "ing", "es"]
		self.word_freq_dict = word_freq_dict
		

	""" 
	Separate a word from its morpheme
	@param word: word to be stemmed 
	@return : no return val
	"""
	def stem_word(self, word): 
		new_word = word 
		for morpheme in self.morphemes: 
			if word.endswith(morpheme):
				len_morpheme = len(morpheme)
    			new_word = new_word[:-len(morpheme)]
    			if self.determine_if_stemmed_word_is_still_real_word(new_word, word):
    				self.word_freq_dict[new_word] = self.word_freq_dict[word]
    				return  new_word
		return word

   	""" 
   	Determine if a word stem is still an acutal word 
	@param stemmed_word: word post-stemming
	@param original_word: word pre-stemming 
	@return : boolean indicating whether stemmed_word is a real word or not 
   	"""
	def determine_if_stemmed_word_is_still_real_word(self, stemmed_word, original_word): 
		pos_extracter = part_of_speech_extracter()
		correct_stemmed_word = pos_extracter.correct_word(stemmed_word)
		if correct_stemmed_word == stemmed_word: 
			return True 
		else: 
			return False

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
