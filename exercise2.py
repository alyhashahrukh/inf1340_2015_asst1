#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# Assignment Outline
# Write a program that determines the name of a shape from its number of sides. Read the number of
# sides from the user and then report the appropriate name as part of a meaningful message. Your program
# should support shapes with anywhere from 3 up to (and including) 10 sides. If the input something other
# than the numbers 3 to 10 then your program should display 'Error'. Your code should be easily readable.
# The function should include comments, proper variable naming and produce messages in case of errors.
# Add your code and test cases to the starter file, exercise2.py, that has been provided. Do not
# change the names of the functions in the file.


def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs:

    Expected Outputs:

    Errors:

    """
# Find shape name by number of sides input by user.

    side = int(input("Please enter the number of sides:"))

    if side == 3:
        print("This is a triangle.")
    elif side == 4:
        print("This is a square.")
    elif side == 5:
        print("This is a pentagon.")
    elif side == 6:
        print("This is a hexagon.")
    elif side == 7:
        print("This is a heptagon.")
    elif side == 8:
        print("This is an octagon.")
    elif side == 9:
        print("This is a nonagon.")
    elif side == 10:
        print("This is a decagon.")

# If sides is 0 or greater than 10 there in no name, therefore "Error" issued.
    if side == 0:
        print ("Error!")
    elif side > 10:
        print ("Error!")

name_that_shape()


# QUESTIONS
# Meaning full message means a proper sentence?
# Does the error statement need to be in a s sentence?
# Comment above need to be filled out or not?