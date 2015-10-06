#!/usr/local/bin/python

'''
    convert.py - Convert a pdf to jpg

    Copyright (C) 2015, Tomasz Finc <tomasz@gmail.com>
    This program is free software; you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation; either version 2 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License along
    with this program; if not, write to the Free Software Foundation, Inc.,
    51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''

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
