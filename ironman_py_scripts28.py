#!/bin/bash/python
#This is python Calculator 

#First Enter Two Numbers 

first_number = int(raw_input("Enter a number "))
second_number = int(raw_input("Enter a number "))
c = 0

def addition(a, b):
	print "Value of a %d b %d c %d"%(first_number, second_number, c)
	return a + b;
def sub(a, b):
	return a - b;
def mul(a, b):
	return a * b;
def divide(a, b):
	return a/b

d=  addition(first_number, second_number)
e = sub(first_number, second_number)
f = mul(first_number, second_number)
g = divide(first_number, second_number)

c= addition(first_number, second_number)	
print(d, e, f, g)






