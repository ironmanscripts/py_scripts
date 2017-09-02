#!/bin/bash/python
#Reading and writing files

from sys import argv

script, filename = argv

print "We're going to erase %r ." %filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that , hit RETURN."

raw_input("?")

print "Opening the file..."
file_stream = open(filename, 'w')

print "Truncationg the file. Good Bye!"
file_stream.truncate()

print "Now I am going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I am going to print these lines to the file."

file_stream.write(line1)
file_stream.write("\n")
file_stream.write(line2)
file_stream.write("\n")
file_stream.write(line3)
file_stream.write("\n")

print "ANd Finally , we close it."
file_stream.close()


