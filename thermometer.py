#!/bin/python

print"This program converts temperatures between Fahrenheit, Celsius, Kelvin, and Bug chirps."
temp, unit = raw_input("Please enter the temperature and the unit (F, C, K, or B): ").split()
temp = int(temp)
print temp
print unit

if unit == "F":
	boop = temp + 10
	print("%d degrees Fahrenheit equals:\n\t%d Celsius\n\t%d Kelvin\n\t%d cricket chirps per minute\n") % (temp, boop, temp, temp)


#write tests first
#include "too hot for crickets" and "too cold for crickets", also a funny message for lower than abs zero
