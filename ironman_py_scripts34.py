#!/bin/bash/python
# Author -- IronMan
# Friday, Sep 8th 2017, time 9:35
# if and else 
# "All comes to those who wait and hustle"

people = 30
cars = 40
trucks = 15

if cars > people:
	print "We should take the cars."
elif cars < people:
	print "We should not take the cars."
else:
	print "We can't decide."

if trucks >cars:
	print "That's too many trucks."
elif trucks < cars:
	print "Maybe we could take the trucks."
else:
	print "We still can't decide."

if people > trucks:
	print "Alright, let's just take the trucks."

else:
	print "Fine, Let's stay home then."


