#!/bin/bash/python
# This program is about virables 

cars =  200
space_in_a_car = 5.0 # always use 5.0, 6.0 due to pemdas error  
drivers = 40.0
passengers = 200.0
cars_not_driven = cars - drivers # _ it is an underscore character 
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are ", cars , "cars available")
print("There are only", drivers ,"drivers available")
print("There will be ", cars_not_driven,"empty cars today.")
print("We can transport ", carpool_capacity, "people today.");
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,"in each car.");



