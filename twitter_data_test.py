import pytest
import sys 

sys.path.insert(0, '/Users/shilpa/CS242/subrahm2/FinalProject')

import keyword_extracting_algorithms
import twitter_data 


def test_correct_output(): 
	""" Test that all the Tweets that have been tweeted so far are being extracted by the twitter_data_wrapper"""

	correct_output = ['This is a tweet about me being excited!', "I'm so excited!", 'Just signed up for Twitter!']
	td = twitter_data.twitter_data('testuser242')
	actual_output = td.twitter_data_wrapper()
	assert correct_output==actual_output