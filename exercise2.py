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

    Actual Outputs: triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, decagon

    Errors: 0 and >10

    Test Case:
    Raw input "1", name output "Error"
    Raw input "2", name output "Error"
    Raw input "3", name output "Triangle"
    Raw input "4", name output "Square"
    Raw input "5", name output "Pentagon"
    Raw input "6", name output "Hexagon"
    Raw input "7", name output "Heptagon"
    Raw input "8", name output "Octagon"
    Raw input "9", name output "Nonagon"
    Raw input "10", name output "Decagon"
    Raw input "11", name output "Error"

    """
    side = int(input("Please enter the number of sides:"))
    

    if side == 3:
        print("Triangle")
    elif side == 4:
        print("Square")
    elif side == 5:
        print("Pentagon")
    elif side == 6:
        print("Hexagon")
    elif side == 7:
        print("Heptagon")
    elif side == 8:
        print("Octagon")
    elif side == 9:
        print("Nonagon")
    elif side == 10:
        print("Decagon")

# If sides are 0 or greater than 10 there is no shape, therefore "Error" issued.

    if side < 3:
        print ("Error")
    elif side > 10:
        print ("Error")

name_that_shape(side)


