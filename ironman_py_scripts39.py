#!/bin/bash/python
# Author- IronMan
# September 10th, 2017
# Sunday time 9:58 am 

ten_things = "Apples Oranges Crows Telephone Light SUgar" # global virable 

print "Wait there are not 10 things in the list. Let's fix that." 

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night","Song","Firebase","Corn","Banana", "Girl", "Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding:", next_one
	stuff.append(next_one)
	print "There are %d items now"% len(stuff)
	
print "There we go:" , stuff

print "Let's do some things with stuff"

print stuff[1]
print stuff[-1] # Whoaa Fancy..
print stuff.pop()
print ''.join(stuff)
print '#'.join(stuff[3:5]) # super stellar!

# Errors in the program:
#	""" Commma Seperator was not included"""



