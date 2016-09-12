#!/usr/bin/env python

'''
Open Source Temperature Conversion Tool

This project is to design a helpful tool to convert between temperature systems, including temperature measured by cricket chirps. The current plan is for all data to be entered manually by the user. However, if you're interested in mobile development and hardware implementation, feel free to create an app that can count chirps automatically.
'''

print"This program converts temperatures between Fahrenheit, Celsius, Kelvin, and Bug chirps."

# Input get and check
str_input = raw_input("Please enter the temperature and the unit (F, C, K, or B): ").split()
if len(str_input) != 2:
        print "Wrong input. format: 40 F"
        exit()

# input separation and conversion
temp, unit = str_input
temp = float(temp)

# print tests, uncomment to print:
# print temp
# print unit

if unit == "F":
        celsius = (temp - 32) * 1.0 / 1.8
        kelvin = (temp + 459.67) * .55
        chirps = (temp - 40) * 4 * 1.0
        print("%f degrees Fahrenheit equals:\n\t%f Celsius\n\t%f Kelvin\n\t%f cricket chirps per minute\n") % (temp, celsius, kelvin, chirps)

if unit == "C":
        fahrenheit = temp * 1.8 + 32
        kelvin = temp + 273.15
        chirps = (fahrenheit - 40) * 4 * 1.0
        print("%f degrees Celsius equals:\n\t%f Fahrenheit\n\t%f Kelvin\n\t%f cricket chirps per minute\n") % (temp, fahrenheit, kelvin, chirps)

if unit == "K":
        celsius = temp - 273.15
        fahrenheit = temp * 1.8 - 459.67
        chirps = (fahrenheit - 40) * 4 * 1.0
        print("%f degrees Kelvin equals:\n\t%f Celsius\n\t%f Fahrenheit\n\t%f cricket chirps per minute\n") % (temp, celsius, kelvin, chirps)

if unit == "B":
        fahrenheit = (temp / 4) + 40
        celsius = (fahrenheit - 32) * 1.0 / 1.8
        kelvin = celsius - 273.15
        print("%f Bug Chirps per minute equals:\n\t%f Celsius\n\t%f Kelvin\n\t%f Fahrenheit\n") % (temp, celsius, kelvin, fahrenheit)        

#nope, didn't make up the cricket thing:  http://www.scientificamerican.com/article/bring-science-home-cricket-temperature/
#write tests first
#needs to handle negatives --I think they are being handled?
#could have better accuracy if using floats not ints everywhere?
#include over 100 F "too hot for crickets" and under 55 F "too cold for crickets", also a funny message for below freezing "cricketsicles don't chirp"?
#include funny message for lower than abs zero
#include funny message about "at -40 it's so cold that no one cares if it's F or C"
#feel free to add Rankine as a unit if you're feeling feisty
