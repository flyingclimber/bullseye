#!/usr/bin/env python

from wand.image import Image
import argparse
import os
import rarfile
import zipfile

RESOLUTION = 300

PARSER = argparse.ArgumentParser(description='Convert pdf to jpg')
PARSER.add_argument('filename', metavar='filename', type=str,
                   help='image to process')
PARSER.add_argument('-o', type=str, help="output file")
PARSER.add_argument('-i', type=int, default=RESOLUTION, help="resolution")

ARGS = PARSER.parse_args()

INPUT_FILE, INPUT_FILE_EXTENSION = os.path.splitext(ARGS.filename)
OUTPUT_FILE = ARGS.o

FILE_NAME = '{}'.format(INPUT_FILE + INPUT_FILE_EXTENSION)

if INPUT_FILE_EXTENSION == '.pdf':
    with Image(filename=FILE_NAME, resolution=RESOLUTION) as pdf:
        print len(pdf.sequence)
        pdf.save(filename=OUTPUT_FILE)
else:
    if INPUT_FILE_EXTENSION == '.cbr':
        ARCHIVE = rarfile.RarFile(FILE_NAME)

    elif INPUT_FILE_EXTENSION == '.cbz':
        ARCHIVE = zipfile.ZipFile(FILE_NAME)

    ARCHIVE.extractall()
