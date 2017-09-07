#!/bin/bash/python
#Written in python 2.7.2
#Author- IronMan
#Time : Written on September 7th, 2017. At 8:12AM in Phoenix 
#Functions Can Return Something 

# Typing this program was a mess in haven't closed fuction delimiters 
# Typo Errors very very dirty
# subtract was subract
# divide was diivide 
# multiply was multply
# """ One Big Mistake is assigning print statemt to print a string lollllllllllll"



def add(a, b):
	print "ADDING %d + %d" %(a, b)
	return a + b;
def subtract(a, b):
	print "SUBRACT %d - %d" %(a, b)
	return a - b;
def multiply(a, b):
	print "Multiply %d * %d"%(a, b)
	return a * b;
def divide(a, b):
	print "DIVIDING %d / %d" %(a, b)
	return a / b;

print "Lets do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)


print "AGe: %d, Height: %d, Weight %d, IQ: %d" %(age, height, weight, iq)


#A puzzle for the extra credit,

print "Here is the puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what , "Can you do it by hand?"


