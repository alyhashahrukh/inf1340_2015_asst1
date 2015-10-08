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

    Expected Outputs: triangle, quadrilateral, pentagon, hexagon, heptagon, octagon, nonagon, decagon

    Actual Outputs: triangle, quadrilateral, pentagon, hexagon, heptagon, octagon, nonagon, decagon

    Errors: < 3 and > 10

    Test Case:
    Raw input "1", name output "Error"
    Raw input "2", name output "Error"
    Raw input "3", name output "triangle"
    Raw input "4", name output "quadrilateral"
    Raw input "5", name output "pentagon"
    Raw input "6", name output "hexagon"
    Raw input "7", name output "heptagon"
    Raw input "8", name output "octagon"
    Raw input "9", name output "nonagon"
    Raw input "10", name output "decagon"
    Raw input "11", name output "Error"

    """
# Create string that finds shape name by number of sides input by user.

    side = raw_input("Please enter the number of sides:")

    if side == "3":
        print("triangle")
    elif side == "4":
        print("quadrilateral")
    elif side == "5":
        print("pentagon")
    elif side == "6":
        print("hexagon")
    elif side == "7":
        print("heptagon")
    elif side == "8":
        print("octagon")
    elif side == "9":
        print("nonagon")
    elif side == "10":
        print("decagon")


# If sides are less than 3 or greater than 10 there is no shape, therefore "Error" issued.
    else:
        print("Error")



#name_that_shape()


