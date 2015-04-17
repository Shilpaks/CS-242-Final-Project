import pytest
import sys
sys.path.insert(0, '/Users/shilpa/CS242/subrahm2/FinalProject')

import lyric_matching
# content of test_sample.py

def test_correct_url_output_lyrics1(): 
	""" Test url generation for lyrics  """

	actual = 'http://api.musixmatch.com/ws/1.1/track.search?q_lyrics=hello-somewhere&apikey=2224fd10c87468942ca6a90f01294452'
	sf = lyric_matching.song_finder(["hello", "somewhere"])
	sf.url_constructer_for_lyrics()
	assert actual == sf.lyric_api_url

def test_correct_url_output_lyrics2(): 
	""" Test url generation for lyrics  """

	actual = 'http://api.musixmatch.com/ws/1.1/track.search?q_lyrics=romeo-somewhere&apikey=2224fd10c87468942ca6a90f01294452'
	sf = lyric_matching.song_finder(["romeo", "somewhere"])
	sf.url_constructer_for_lyrics()
	assert actual == sf.lyric_api_url

def test_correct_url_output_lyrics3(): 
	""" Test url generation for lyrics  """

	actual = 'http://api.musixmatch.com/ws/1.1/track.search?q_lyrics=hello&apikey=2224fd10c87468942ca6a90f01294452'
	sf = lyric_matching.song_finder(["hello"])
	sf.url_constructer_for_lyrics()
	assert actual == sf.lyric_api_url

def test_correct_url_output_lyrics4(): 
	""" Test url generation for lyrics  """

	actual = 'http://api.musixmatch.com/ws/1.1/track.search?q_lyrics=hello-there-everyone&apikey=2224fd10c87468942ca6a90f01294452'
	sf = lyric_matching.song_finder(["hello", "there", "everyone"])
	sf.url_constructer_for_lyrics()
	assert actual == sf.lyric_api_url

def test_correct_url_output_chart1(): 
	""" Test url generation for chart songs """

	actual = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?page_size=1&country=us&apikey=2224fd10c87468942ca6a90f01294452'
	sf = lyric_matching.song_finder(["romeo", "somewhere"])
	sf.url_constructer_for_chart_songs("us")
	assert actual == sf.chart_url

def test_correct_url_output_chart2(): 
	""" Test url generation for chart songs """

	actual = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?page_size=1&country=it&apikey=2224fd10c87468942ca6a90f01294452'
	sf = lyric_matching.song_finder(["hello", "somewhere"])
	sf.url_constructer_for_chart_songs("it")
	assert actual == sf.chart_url

def test_correct_url_output_chart3(): 
	""" Test url generation for chart songs """

	actual = 'http://api.musixmatch.com/ws/1.1/chart.tracks.get?page_size=1&country=uk&apikey=2224fd10c87468942ca6a90f01294452'
	sf = lyric_matching.song_finder(["what", "somewhere"])
	sf.url_constructer_for_chart_songs("uk")
	assert actual == sf.chart_url

def test_determine_if_valid_results_exist(): 
	""" Test if there is a need to determine a popular song to recommend """

	sf = lyric_matching.song_finder(["romeo", "somewhere"])
	assert sf.determine_if_valid_results_exist() == False