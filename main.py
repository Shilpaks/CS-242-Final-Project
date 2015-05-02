#!/usr/bin/env python

import twitter_data 
import text_message 
import credentials 
import spell_checker 
import keyword_extracting_algorithms 
import lyric_matching 
import twitter_user 
import user


def main(): 

	""" Initialize the subscription handler and determine the list of users to whom we 
	need to send recommendations """ 
	subscription_handler = text_message.subscription_handler()
	subscription_handler.handle_subscriptions()

	user_recipient_list = subscription_handler.recipient_list


	for user in user_recipient_list: 
		""" Initialize Twitter data object and get tweets object """ 
		td = twitter_data.twitter_data(user.twitter_username)

		#td = twitter_data.twitter_data('testuser242')
		tweets = td.twitter_data_wrapper()

		""" Initialize part of speech extracter object """ 
		pos_extracter = keyword_extracting_algorithms.part_of_speech_extracter()

		""" Obtain keywords from recent tweets by extracting only the nouns and verbs """ 

		keywords = pos_extracter.parse_nouns_and_verbs(tweets)

		keyword_list = list(keywords.keys())

		""" Obtain a song that matches the keywords previously generated """ 

		song_finder = lyric_matching.song_finder(keyword_list)

		song_finder.find_song()

		song_url = song_finder.song_url 
		song_artist = song_finder.song_artist 
		song_title = song_finder.song_title
		
		""" Format the text message to be sent that includes song information """ 


		message_formatter = text_message.message_formatter(song_artist, song_title, song_url)

		message_author_title_url = message_formatter.format_message_author_title_url()
		message_url = message_formatter.format_message_url()

		""" Actually send the text message to the recipient""" 

		text_messager= text_message.text_messager(user.phone_number)
		text_messager.send_message(message_author_title_url)
		#text_messager.send_message(message_url)




if __name__ == '__main__':
  	main()