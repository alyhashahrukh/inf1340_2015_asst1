#!/usr/bin/env python

""" Assignment 1, Exercise 3, INF1340, Fall, 2015. Troubleshooting Car Issues.

This module contains one function diagnose_car(). It is an expert system to
interactive diagnose car issues.

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def diagnose_car(answer):
    """
    Interactively queries the user with yes/no questions to identify a
    possible issue with a car.
    Inputs:
    Expected Outputs:
    Errors:
    """

    if answer == 'y':
        question1 = "Are the battery terminals corroded?"
        question2 = raw_input(question1)
        if question2 == 'y':
            question3 = "Clean terminals and try starting again"
            print (question3)
        elif question2 == 'n':
            question3 = "Replace cables and try again"
            print(question3)
        else:
            print("Incorrect entry, start over")
    elif answer == 'n':
        question1 = "Does the car make a clicking noise?"
        question2 = raw_input(question1)
        if question2 == 'y':
            print("Replace battery")
        elif question2 == 'n':
            question3 = "Does the car crank up but fail to start?"
            question4 = raw_input(question3)
            if question4 == 'y':
                print("Check spark plug connections")
            elif question4 == 'n':
                question5 = "Does the engine start and then die?"
                question6 = raw_input(question5)
                if question6 == 'y':
                    question7 = "Does your car have fuel injection?"
                    question8 = raw_input(question7)
                    if question8 == 'y':
                        print("Get it in for service!")
                    elif question8 == 'n':
                        print("Check to ensure the choke is opening and closing")
                    else:
                        print("Incorrect entry, start over")
                elif question6 == 'n':
                    print("No answer can be provided")   #No section to diagram, check with Prof/TA
                else:
                    print("Incorrect entry, start over")
            else:
                print("Incorrect entry, start over")
        else:
            print("Incorrect entry, start over")
    else:
        print("Incorrect entry, start over")


diagnose_car(raw_input("Is the car silent when you turn it on?"))












