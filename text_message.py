from twilio.rest import TwilioRestClient
import credentials 
from flask import Flask, request, redirect
import twilio.twiml
import user


class subscription_handler(object): 

	def __init__(self): 
		self.recipient_list = [] # list of user objects
		self.recipient = "+17084261628"
		self.recipient_set = set() #primarily for book keeping 


	def message_parser(self, message_sender_tuple):
		""" Parse a list of message-sender tuples and call the appropriate function: sign_up or stop_messages 
		@param message_sender_tuple: tuple in which first argument is body of message and second argument is the sender's number

		""" 

		body = message_sender_tuple[0]
		sender = message_sender_tuple[1]
		if body.startswith("STOP"):
			self.stop_messages(message, body, sender)
		elif body.startswith("SIGNUP"):
			self.sign_up(body, sender) 

	def sign_up(self, message, sender):
		""" Create a user object for a given person and add the object to the recipient_list
		@param message: body of text message
		@param sender: sender of text message 
		""" 

		split_vals = message.split(" ")
		que = split_vals.pop(0)
		username = " ".join(split_vals)
		if sender not in self.recipient_set: 
			new_user = user.user(username, sender)
			self.recipient_set.add(sender)
			self.recipient_list.append(new_user)

	def stop_messages(self, message, sender):
		""" Remove a specific person from the recipient_list
		@param message: body of text message 
		@param sender: sender of text message
		""" 

		split_vals = message.split(" ")
		que = split_vals.pop(0)
		username = " ".join(split_vals)
		for each in self.recipient_list: 
			if each.phone_number == sender: 
				self.recipient_list.remove(each)
				self.recipient_set.remove(each)

	def get_new_messages(self): 
		""" Get all the new messages (sign ups and subscription cancellations)
		@return : list of tuples. first argument of tuple is message body, second argument of tuple is the sender of the message 
		""" 

		account_sid = credentials.account_sid
		auth_token  = credentials.auth_token
		client = TwilioRestClient(account_sid, auth_token)
		messages = client.messages.list(to=self.recipient)
		return [tuple([str(message.body), str(message.from_ )]) for message in messages]


	def handle_subscriptions(self): 
		""" Wrapper for the class' functionality """ 

		message_sender_tuples = self.get_new_messages()
		for tup in message_sender_tuples: 
			self.message_parser(tup)




class text_messager(object):
	""" Class that is responsible for actually sending out text messages """ 

	def __init__(self, recipient):
		self.sender = "+17084261628"
		self.recipient = "+16307703769"


	def send_message(self, message): 
		""" Send the actual text message """ 

		""" Authentication for the Twilo API """ 
		account_sid = credentials.account_sid
		auth_token  = credentials.auth_token

		""" Initialize Twilo Client """ 
		client = TwilioRestClient(account_sid, auth_token)

 		""" Send the message with parameters: body, to, and from """ 


		message = client.messages.create(to=self.recipient, 
			from_=self.sender,
			body=message)



class message_formatter(object): 
	""" Class that is responsible for formatting the messages that are to be sent by
	the text_messager class """ 

	def __init__(self, artist, song_name, song_url): 
		self.artist = artist
		self.song_name = song_name
		self.url = song_url

	def format_message_author_title_url(self): 
		final_message =  "Your song recommendation:\n"
		artist_str = "Artist: " + self.artist + "\n"
		song_name_str = " \n Title: " + self.song_name + "\n"
		song_url = "URL: " +  self.url + "\n"
		return final_message + song_name_str + artist_str + song_url 

	def format_message_url(self): 
		final_message = " \n Song URL: "
		final_message = final_message + self.url + "\n"
		return final_message
""" Test code """ 

#msg = get_new_messages()
#print msg.get_new_messages()

# handler = subscription_handler()
# handler.handle_subscriptions()
# print [user.twitter_username for user in handler.recipient_list]
# formatter = message_formatter("Taylor Swift", "Love Story", "https://google.com")
# messager = text_messager(formatter.format_message(), "+16307703769")
# messager.send_message()