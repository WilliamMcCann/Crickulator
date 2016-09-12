#!/usr/bin/env python
import argparse
import sys
from conversions import conversions

def convert(args):
    if args.input not in conversions:
        print args.input, "is not a recognized unit."
        sys.exit(1)
    if args.output not in conversions:
        print args.output, "is not a recognized unit."
        sys.exit(1)

    input_unit = conversions[args.input]
    output_unit = conversions[args.output]

    if input_unit.get_category() != output_unit.get_category():
        print "%s cannot be converted to %s." % (input_unit.get_name(), output_unit.get_name())
        sys.exit(1)

    value_in_base_units = input_unit.convert_to_base(args.to_convert[0])
    value_in_output_units = output_unit.convert_from_base(value_in_base_units)

    print value_in_output_units


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This program converts temperatures between Fahrenheit, Celsius, Kelvin, and Bug chirps.")
    parser.add_argument("to_convert", metavar="N", type=float, nargs=1, help="The value to convert")
    parser.add_argument("-i", "--input", help="The units of N", required=True)
    parser.add_argument("-o", "--output", help="The units of the result", required=True)

    args = parser.parse_args()
    convert(args)

#nope, didn't make up the cricket thing:  http://www.scientificamerican.com/article/bring-science-home-cricket-temperature/
#write tests first
#needs to handle negatives --I think they are being handled?
#include over 100 F "too hot for crickets" and under 55 F "too cold for crickets", also a funny message for below freezing "cricketsicles don't chirp"?
#include funny message for lower than abs zero
#include funny message about "at -40 it's so cold that no one cares if it's F or C"
#feel free to add Rankine as a unit if you're feeling feisty
