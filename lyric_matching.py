import credentials 
import urllib
import json

""" 
SongFinder class. Constructor takes in a list of keywords. To access song title, artist, or video/lyric url of recommended song, 
print song_title, song_artist, and song_url respectively 

"""
class song_finder(object): 

  def __init__(self, keyword_list): 

    self.keyword_list = keyword_list
    self.API_key = credentials.musix_match_api_key
    self.root_url = 'http://api.musixmatch.com/ws/1.1/'
    self.method = 'track.search?q_lyrics='
    self.lyric_api_url = None 
    self.lyric_data = None
    self.song_url = None
    self.song_artist = None
    self.song_title = None

    self.chart_url = None
    self.chart_data = None


  def url_constructer_for_lyrics(self):
    """ Construct the URL that is needed to access the music data from the MusixMatch database """ 

    self.lyric_api_url = self.root_url + self.method
    keyword_string = "-".join(self.keyword_list)
    self.lyric_api_url = self.lyric_api_url + keyword_string +"&apikey=" + self.API_key

  def get_lyric_data(self): 
    """ Get the data from the MusixMatch database in JSON form and write the JSON data to the class attribute "data" """ 

    response = urllib.urlopen(self.lyric_api_url)
    self.lyric_data = json.loads(response.read())
  
  def determine_if_valid_results_exist(self): 
    """
    Determine if valid song suggestions exist based on input lyrics 
    @return True if valid results exist, False otherwise 
    """
    if self.lyric_data == None: 
      return False
    track_data = self.lyric_data['message']['header']['available']
    if track_data == 0: 
      return False
    else: 
        return True 

  def parse_lyric_data(self):
    """ 
    Parse the JSON data in the class attribute "lyric_data" and store the results (arist name, track name, and url) in class member variable fields: 
    song_artist, song_title, song_url (respectively)
    """

    track_data = self.lyric_data['message']['body']['track_list'][0]['track']
    self.song_url = track_data['track_edit_url']
    self.song_title= track_data['track_name']
    self.song_artist = track_data['artist_name']

  def popular_song_picker(self):
    """ Pick a popular, chart-topping song if mining of lyrics was unsuccessful """ 

    if self.determine_if_valid_results_exist() == False: 
      self.url_constructer_for_chart_songs("us")
      self.get_popular_song_data()
      self.parse_chart_data()

  def url_constructer_for_chart_songs(self, user_country): 
    """ Construct the URL that is needed to access the music data from the MusixMatch database """ 

    self.chart_url = self.root_url + "chart.tracks.get?page_size=1&country=" + user_country +"&apikey=" + self.API_key

  def get_popular_song_data(self): 
    """ Get the data from the MusixMatch database in JSON form and write the JSON data to the class attribute "data" """ 

    response = urllib.urlopen(self.chart_url)
    self.chart_data = json.loads(response.read())
  
  def parse_chart_data(self):
    """ 
    Parse the JSON data in the class attribute "chart_data" and store the results (arist name, track name, and url) in class member variable fields: 
    song_artist, song_title, song_url (respectively)
    """

    track_data = self.chart_data['message']['body']['track_list'][0]['track']
    self.song_url = track_data['track_edit_url']
    self.song_title= track_data['track_name']
    self.song_artist = track_data['artist_name']

  def find_song(self): 
    """ Wrapper for the whole class' functionality """
    self.url_constructer_for_lyrics(self.keyword_list)
    self.get_lyric_data()
    self.parse_lyric_data()
    self.popular_song_picker()










