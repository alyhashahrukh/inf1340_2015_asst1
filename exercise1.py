#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"

# Test case:
# If transaction_money_difference = -$25065 then code is functioning correctly
# No user input = no errors



# Set original problem variables

purchased_shares = 2000
share_purchase_price = 900.00
commission_percentage = 0.03
sold_shares = 2000
share_selling_price = 942.75

#Calculate the amount paid for initial purchase of 2000 shares

cost_of_shares = (purchased_shares * share_purchase_price)
purchase_commission_cost = (cost_of_shares * commission_percentage)
total_purchase_cost = (cost_of_shares + purchase_commission_cost)

#Calculate the amount made for the sale of her 2000 shares

share_sale_profit = (sold_shares * share_selling_price)
sale_commission_cost = (share_sale_profit * commission_percentage)
total_sale_profit = (share_sale_profit - sale_commission_cost)

#Calculate the amount of money remaining after stock transactions

transaction_money_difference = (total_sale_profit - total_purchase_cost)

#Translate numerical calculations to a profit or loss position

if transaction_money_difference < 0:
    print("Lakshmi recorded a loss on the transaction of $"),abs(transaction_money_difference)
else:
    print ("Lakshmi recorded a profit on the transaction of $"),(transaction_money_difference)







