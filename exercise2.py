#!/usr/bin/env python

""" Assignment 1, Exercise 2, INF1340, Fall, 2015. Name that shape.

This module contains one function name_that_shape(). It prompts the user
to input the number of sides in a shape and outputs the name of the shape.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"



def name_that_shape():
    """
    For a given number of sides in a regular polygon, returns the shape name

    Inputs: 3 to 10

    Expected Outputs: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

    Errors: 0 and >10

    Test Case: To test this code we input numbers between 3 and 10 to see if the number
    of sides would result in the accurate shape name as an output; we further entered
    numbers < 3 and > 10 to see if an error message showed. Through this testing we are
    certain that the number of sides correlate with the correct shape name statement.

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

# If sides are 0 or greater than 10 there is no shape, therefore "Error" issued.

    if side < 3:
        print ("Error!")
    elif side > 10:
        print ("Error!")

name_that_shape()


