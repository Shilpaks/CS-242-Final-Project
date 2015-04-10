import pytest
import keyword_extracting_algorithms
# content of test_sample.py

def set_up_parse_nouns_and_verbs(list1): 
	dictionary = {}
	for each in list1: 
		freq = dictionary.get(each, 0)
		freq += 1 
		dictionary[each] = freq
	return dictionary 

def test_parse_nouns_and_verbs1():
	dictionary = set_up_parse_nouns_and_verbs(["beach", "run"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary==pos_extracter.parse_nouns_and_verbs(["he", "run", "beach"]))

def test_parse_nouns_and_verbs2():
	dictionary = set_up_parse_nouns_and_verbs(["he", "beach", "run"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary!=pos_extracter.parse_nouns_and_verbs(["he", "run", "beach"]))

def test_parse_nouns_and_verbs3():
	dictionary = set_up_parse_nouns_and_verbs(["he", "she"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary!=pos_extracter.parse_nouns_and_verbs(["he", "run", "beach"]))

def test_parse_nouns_and_verbs4():
	dictionary = set_up_parse_nouns_and_verbs(["walking", "yellow"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary!=pos_extracter.parse_nouns_and_verbs(["yellow", "wallking", "he"]))

def test_parse_nouns_and_verbs5():
	dictionary = set_up_parse_nouns_and_verbs(["Twitter", "run"])
	pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

	assert (dictionary==pos_extracter.parse_nouns_and_verbs(["Twitter", "run"]))
