#!/bin/python

print"This program converts temperatures between Fahrenheit, Celsius, Kelvin, and Bug chirps."
temp, unit = raw_input("Please enter the temperature and the unit (F, C, K, or B): ").split()
temp = int(temp)
print temp
print unit

if unit == "F":
        celsius = ((temp - 32) * 1.0) / 1.8
        kelvin = (temp + 459.67) * .55
        chirps = ((temp - 40) *1.0) * 4
        print("%d degrees Fahrenheit equals:\n\t%d Celsius\n\t%d Kelvin\n\t%d cricket chirps per minute\n") % (temp, celsius, kelvin, chirps)

if unit == "C":
        fahr = ((temp * 1.8) + 32
        kelvin = temp + 273.2
        chirps = ((temp - 8) * 6.0
        print("%d degrees Celsius equals:\n\t%d Fahrenheit\n\t%d Kelvin\n\t%d cricket chirps per minute\n") % (temp, celsius, kelvin, chirps)

if unit == "K":
        celsius = ((temp - 32) * 1.0) / 1.8
        kelvin = (temp + 459.67) * .55
        chirps = ((temp - 40) *1.0) * 4
        print("%d degrees Fahrenheit equals:\n\t%d Celsius\n\t%d Kelvin\n\t%d cricket chirps per minute\n") % (temp, celsius, kelvin, chirps)

if unit == "B":
        celsius = ((temp - 32) * 1.0) / 1.8
        kelvin = (temp + 459.67) * .55
        chirps = ((temp - 40) *1.0) * 4
        print("%d degrees Fahrenheit equals:\n\t%d Celsius\n\t%d Kelvin\n\t%d cricket chirps per minute\n") % (temp, celsius, kelvin, chirps)





#nope, didn't make up the cricket thing:  http://www.scientificamerican.com/article/bring-science-home-cricket-temperature/
#write tests first
#needs to handle negatives
#include over 100 F "too hot for crickets" and under 55 F "too cold for crickets", also a funny message for below freezing "cricketsicles don't chirp"?
#include funny message for lower than abs zero
#include funny message about "at -40 it's so cold that no one cares if it's F or C"
