#!/usr/bin/env python

'''
    reviewbox.py - Given a classifier tag an image
'''

import cv2
import argparse

PARSER = argparse.ArgumentParser(description='Given a classifier tag an image')
PARSER.add_argument('filename', metavar='filename', type=str, nargs='*',
                   help='image to process')
PARSER.add_argument('-s', type=float, default=0.5, help='scaling factor')
PARSER.add_argument('-n', action="store_true",
                    help='dry run, only output changed files')

ARGS = PARSER.parse_args()

CASCADE = 'training/data/cascade.xml'
IMAGE_LIST = ARGS.filename
SCALING = ARGS.s
DRYRUN = ARGS.n

CLASSIFIER = cv2.CascadeClassifier(CASCADE)

for image in IMAGE_LIST:
    IMG = cv2.imread(image)
    GRAY = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
    MATCH = CLASSIFIER.detectMultiScale(GRAY, 1.3, 5)

    if ARGS.n:
        print "{} {}".format(image, len(MATCH))
    else:
        for (x, y, w, h) in MATCH:
            cv2.rectangle(IMG, (x, y), (x+w, y+h), (255, 0, 0), 2)

        RES = cv2.resize(IMG, None, fx=SCALING, fy=SCALING,
                         interpolation=cv2.INTER_CUBIC)
        cv2.imshow('Sample', RES)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
