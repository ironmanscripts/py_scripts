#!/bin/bash/python
# Author - IronMan
# September 2017, time 11:12am

# Class

class Song(object):
	
#	def __init__(self, lyrics):
#		self.lyrics = lyrics
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line

happy_bday = Song(["Happy Birthday to you"])

bulls_on_parade = Song(["They rally around the family"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

