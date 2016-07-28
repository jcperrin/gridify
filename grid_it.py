#!usr/bin/python

#import modules
from PIL import Image #library for manipulating imgs
import logging
import os
import sys

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITICAL)

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

def get_img(img):
    logging.debug('getting img')
    return "img.png"

def change_img(img):
    logging.debug('changing img')
    return "new_img.txt"

def save_img(img):
    logging.debug('saving img')
    

def main():
    logging.debug('Start of the program.')
    fname = get_filename()
    img = get_img(fname)
    output = change_img(img)
    save_img(output)
    logging.debug('End of program.')

if __name__ == "__main__":
    main()
