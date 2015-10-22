#!/usr/local/bin/python

'''
    reviewbox.py - Given a classifier tag an image
'''

import cv2
import argparse

PARSER = argparse.ArgumentParser(description='Given a classifier tag an image')
PARSER.add_argument('filename', metavar='filename', type=str,
                   help='image to process')
PARSER.add_argument('-s', type=float, default=1, help='scaling factor')

ARGS = PARSER.parse_args()
SCALING = ARGS.s

CASCADE = 'training/data/cascade.xml'
SRC_IMAGE = ARGS.filename

CLASSIFIER = cv2.CascadeClassifier(CASCADE)

IMG = cv2.imread(SRC_IMAGE)
GRAY = cv2.cvtColor(IMG, cv2.COLOR_BGR2GRAY)
MATCH = CLASSIFIER.detectMultiScale(GRAY, 1.3, 5)

for (x, y, w, h) in MATCH:
    cv2.rectangle(IMG, (x, y), (x+w, y+h), (255, 0, 0), 2)

RES = cv2.resize(IMG, None, fx=SCALING, fy=SCALING,
                 interpolation=cv2.INTER_CUBIC)
cv2.imshow('Sample', RES)
cv2.waitKey(0)
cv2.destroyAllWindows()
