#!/usr/bin/env python
import argparse

def convert(args):
    # This function needs a better way to check inputs
    if args.input == "fahrenheit":
        function = {
            "celsius": lambda temp: (temp - 32) / 1.8,
            "kelvin": lambda temp: (temp + 459.67) * .55,
            "chirps": lambda temp: (temp - 40) * 4
        }[args.output]
    else:
        raise Exception("Only fahrenheit support currently")
    print function(args.to_convert[0])



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program converts temperatures between Fahrenheit, Celsius, Kelvin, and Bug chirps.")
    parser.add_argument("to_convert", metavar="N", type=float, nargs=1, help="The value to convert")
    parser.add_argument("-i", "--input", help="The units of N", required=True)
    parser.add_argument("-o", "--output", help="The units of the result", required=True)

    args = parser.parse_args()
    convert(args)

#nope, didn't make up the cricket thing:  http://www.scientificamerican.com/article/bring-science-home-cricket-temperature/
#write tests first
#needs to handle negatives
#could have better accuracy if using floats not ints everywhere?
#include over 100 F "too hot for crickets" and under 55 F "too cold for crickets", also a funny message for below freezing "cricketsicles don't chirp"?
#include funny message for lower than abs zero
#include funny message about "at -40 it's so cold that no one cares if it's F or C"
#feel free to add Rankine as a unit if you're feeling feisty
