#!/usr/local/bin/python

from wand.image import Image
import argparse

RESOLUTION = 300

PARSER = argparse.ArgumentParser(description='Convert pdf to jpg')
PARSER.add_argument('-f', type=str, help="pdf to read")
PARSER.add_argument('-o', type=str, help="output file")
PARSER.add_argument('-i', type=int, default=RESOLUTION, help="resolution")

ARGS = PARSER.parse_args()

INPUT_FILE = ARGS.f
OUTPUT_FILE = ARGS.o

FILE_NAME = '{}'.format(INPUT_FILE)

with Image(filename=FILE_NAME, resolution=RESOLUTION) as pdf:
    print len(pdf.sequence)
    pdf.save(filename=OUTPUT_FILE)
