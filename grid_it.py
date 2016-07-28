#!usr/bin/python

#import modules
from PIL import Image #library for manipulating imgs
import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

#"Constants"
NUM_COLS = 2
NUM_ROWS = 2

#this function prompts the user for a valid file name
#it loops until a valid name is entered
#
# TODO: Test if the file is a valid image file
def get_filename():
    logging.debug('getting file')
    while True:
        name = raw_input('Enter q to quit\nFile name: ')
        if os.path.isfile(name) | (name is 'q'):
            break
        else:
            print('File not found.\n')
    return name

#This funciton opens and sets up the image for manipulation
def get_img(fname):
    logging.debug('getting img')
    return Image.open(fname)

#this function does the actual image manipulation
#The change intended is to create a grid of spread blocks
#ultimately, the blocks will be sampled from overlapping frames
def change_img(img):
    logging.debug('changing img')
    logging.debug( img.size)
    img_width, img_height = img.size
    logging.debug(img_width)
    logging.debug(img_height)

    pane_width = img_width / NUM_COLS
    pane_height = img_height / NUM_ROWS
    panes = [[0 for x in range(NUM_COLS)] for y in range(NUM_ROWS)]
    for x in range(NUM_COLS):
        for y in range(NUM_ROWS):
            ulx = x * pane_width
            uly = y * pane_height
            pane = (ulx, uly, ulx + pane_width, uly + pane_height)
            panes[x][y] = img.crop(pane)
     
    return "new_img.txt"

def save_img(img):
    logging.debug('saving img')
    

def main():
    logging.debug('Start of the program.')
   # fname = get_filename()
    fname = 'face.jpg'
    img = get_img(fname)
    output = change_img(img)
    save_img(output)
    logging.debug('End of program.')

if __name__ == "__main__":
    main()

