#!/bin/bash/python
# Written in Python 2.7.2
# Author - IRON-MAN
# Python More Practice 
# Coded on Thursday Sep 7th 2017, Time 9:55am.




def break_words(stuff):
	""" This function will break up words for us"""
	words = stuff.split(' ')
	return words

def sort_words(words):
	"""Sorts the words"""
	return sorted(words)

def print_first_word(words):
	"""print the first words after popping if off"""
	word = words.pop(0)
	print word

def print_last_word(words):
	"""Takes in a full sentence and returns the sorted words."""
	word = words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Takes in a full sentence and returns the sorted words."""
	words = break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""prints the first and last words of the sentence."""
	words = break_words(sentence)
	print_first_word(words)
	print_last_word(words)

def print_first_and_last_sorted(sentence):
	"""Sorts the words then prints the first and last one."""
	words = sort_sentence(sentence)
	print_first_word(words)
	print_last_word(words)


