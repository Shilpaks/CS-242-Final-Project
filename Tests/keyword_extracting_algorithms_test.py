import pytest
import sys
sys.path.insert(0, '/Users/shilpa/CS242/subrahm2/FinalProject')

import keyword_extracting_algorithms

def set_up_parse_nouns_and_verbs(list1): 
	dictionary = {}
	for each in list1: 
		freq = dictionary.get(each, 0)
		freq += 1 
		dictionary[each] = freq
	return dictionary 

def test_parse_nouns_and_verbs1():
	""" Test that the part of speech extracter is extracting only nouns and verbs """

	dictionary = set_up_parse_nouns_and_verbs(["beach", "run"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary==pos_extracter.parse_nouns_and_verbs(["he", "run", "beach"]))

def test_parse_nouns_and_verbs2():
	""" Test that the part of speech extracter is extracting only nouns and verbs """

	dictionary = set_up_parse_nouns_and_verbs(["he", "beach", "run"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary!=pos_extracter.parse_nouns_and_verbs(["he", "run", "beach"]))

def test_parse_nouns_and_verbs3():
	""" Test that the part of speech extracter is extracting only nouns and verbs """

	dictionary = set_up_parse_nouns_and_verbs(["he", "she"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary!=pos_extracter.parse_nouns_and_verbs(["he", "run", "beach"]))

def test_parse_nouns_and_verbs4():
	""" Test that the part of speech extracter is extracting only nouns and verbs """

	dictionary = set_up_parse_nouns_and_verbs(["walking", "yellow"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary!=pos_extracter.parse_nouns_and_verbs(["yellow", "wallking", "he"]))

def test_parse_nouns_and_verbs5():
	""" Test that the part of speech extracter is extracting only nouns and verbs """

	dictionary = set_up_parse_nouns_and_verbs(["twitter", "run"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary==pos_extracter.parse_nouns_and_verbs(["twitter", "run"]))

def test_spell_check1(): 
	""" Test spell checker for word off by 1 edit """

	word = "helllo"
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()
	correction = pos_extracter.correct_word(word)
	assert "hello" == correction

def test_spell_check2(): 
	""" Test spell checker for word off by 1 edit """

	word = "raan"
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()
	correction = pos_extracter.correct_word(word)
	assert "ran" == correction

def test_spell_check3(): 
	""" Test spell checker for word off by more than 2 edits """

	word = "skdjfaksldfj"
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()
	correction = pos_extracter.correct_word(word)
	assert "skdjfaksldfj" == correction

def test_spell_check4(): 
	""" Test spell checker for word off by 0 edits """

	word = "correct"
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()
	correction = pos_extracter.correct_word(word)
	assert "correct" == correction

def test_tfidf_term_frequency1(): 
	""" Test TF-IDF frequency calculations  """

	tfidf = keyword_extracting_algorithms.tf_idf(["apple", "apple", "apple"], ["apple", "apple", "banana"])
	actual = tfidf.find_term_frequency ("apple", ["apple", "apple", "banana"])
	assert actual == 2

def test_tfidf_term_frequency2(): 
	""" Test TF-IDF frequency calculations  """

	tfidf = keyword_extracting_algorithms.tf_idf(["apple", "orange", "banana"], ["apple", "apple", "banana"])
	actual = tfidf.find_term_frequency ("apple", ["apple", "orange", "banana"])
	assert actual == 1

def test_tfidf_main(): 
	""" Test main tf-idf weighting scheme  """

	tfidf = keyword_extracting_algorithms.tf_idf(["apple", "orange", "banana"], ["apple", "apple", "banana"])
	actual = tfidf.tf_idf("apple")
	assert actual == 1.0986122886681098