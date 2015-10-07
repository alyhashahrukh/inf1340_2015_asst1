#!/usr/bin/env python

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module prints the amount of money that Lakshmi has remaining
after the stock transactions

"""

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


# Assignment Outline
# Lakshmi bought 2000 shares.
# When Lakshmi purchased the stock, she paid $900.00 per share.
# Lakshmi paid her stockbroker a commission that amounted to 3 percent of the amount she paid for the stock
# Lakshmi sold 2000 shares.
# She sold the stock for $942.75 per share.
# She paid his stockbroker another commission that amounted to 3 percent of the amount she received for the stock.

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

# Test case: To test this code to see if it runs properly, we checked the answer the program
# generates with the correct answer we calculated on our own. We preformed this same test
# again with another different variables. When both tests matched the same answers the
# program came up with we knew the program was functioning correctly



#Questions to ask professor/TA
# 1) Should there be anymore displayed print or just the answer statement?
# 2) Is the if statement ok or should it actually display a negative number?
# 3) Are the comments descriptive enough?



