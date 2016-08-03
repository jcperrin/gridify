#!usr/bin/python

#import modules
from PIL import Image #library for manipulating imgs
import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

#"Constants"
NUM_COLS = 4
NUM_ROWS = 5
PANE_SPACING = 10

#this function prompts the user for a valid file name
#it loops until a valid name is entered
#
# TODO: Test if the file is a valid image file
def get_filename():
    logging.debug('getting file')
    if os.path.isfile(name) | (name is 'q'): 
        return NULL
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
    pane_width = 2 * img_width / (NUM_COLS + 1)
    pane_height = 2 * img_height / (NUM_ROWS + 1)
    panes = divide_into_panes(img, pane_width, pane_height)
    canvas = create_blank_canvas(pane_width, pane_height)
    final = paste_panes(canvas, panes)
    final.show()
    return "new_img.txt"

# this function merges the panes and canvas into one image
def paste_panes(canvas, panes):
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            pane = panes[col][row]
            (w, h) = pane.size
            canvas.paste(pane, ((PANE_SPACING+w) * col,
                (h+PANE_SPACING) * row))
    return canvas

# this function creates a correctly sized blank canvas for the 
# photos to be placed on
# default color of the canvas is white
# eventually extendable to have varying space widths
def create_blank_canvas(pane_width, pane_height):
    logging.debug('create blank canvas')
    canvas = Image.new("RGB",((pane_width + PANE_SPACING) * NUM_COLS -
            PANE_SPACING,(pane_height + PANE_SPACING) * NUM_ROWS -
            PANE_SPACING), "white")
    return canvas

# this function creates a NUM_COLS by NUM_ROWS array of
# 'sub-photos'
def divide_into_panes(img, pane_width, pane_height):
    logging.debug('divide into panes')
    panes = [[0 for row in range(NUM_ROWS)] for col in range(NUM_COLS)]
    for col in range(NUM_COLS):
        for row in range(NUM_ROWS):
            ulx = col * pane_width / 2
            uly = row * pane_height / 2
            pane = (ulx, uly, ulx + pane_width, uly + pane_height)
            panes[col][row] = img.crop(pane)
    return panes
    
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

