#!/usr/bin/env python3

# Created By: Liam Csiffary
# Date: May 4, 2021
# This program calculates the cost
# of a pizza order


# import the constants from constants.py
import constants


# create the order_pizza function
def order_pizza():
    num_of_pizzas = int(input("How many pizzas are you ordering(MAX6): "))

    # asks the user the diameter of their pizzas depending
    # on how many pizzas they wanted
    if num_of_pizzas == 1:
        diam_of_pizza1 = float(input("Diameter of pizza 1: "))
        diam_of_pizza2 = 0
        diam_of_pizza3 = 0
        diam_of_pizza4 = 0
        diam_of_pizza5 = 0
        diam_of_pizza6 = 0

    if num_of_pizzas == 2:
        diam_of_pizza1 = float(input("Diameter of pizza 1: "))
        diam_of_pizza2 = float(input("Diameter of pizza 2: "))
        diam_of_pizza3 = 0
        diam_of_pizza4 = 0
        diam_of_pizza5 = 0
        diam_of_pizza6 = 0

    if num_of_pizzas == 3:
        diam_of_pizza1 = float(input("Diameter of pizza 1: "))
        diam_of_pizza2 = float(input("Diameter of pizza 2: "))
        diam_of_pizza3 = float(input("Diameter of pizza 3: "))
        diam_of_pizza4 = 0
        diam_of_pizza5 = 0
        diam_of_pizza6 = 0

    if num_of_pizzas == 4:
        diam_of_pizza1 = float(input("Diameter of pizza 1: "))
        diam_of_pizza2 = float(input("Diameter of pizza 2: "))
        diam_of_pizza3 = float(input("Diameter of pizza 3: "))
        diam_of_pizza4 = float(input("Diameter of pizza 4: "))
        diam_of_pizza5 = 0
        diam_of_pizza6 = 0

    if num_of_pizzas == 5:
        diam_of_pizza1 = float(input("Diameter of pizza 1: "))
        diam_of_pizza2 = float(input("Diameter of pizza 2: "))
        diam_of_pizza3 = float(input("Diameter of pizza 3: "))
        diam_of_pizza4 = float(input("Diameter of pizza 4: "))
        diam_of_pizza5 = float(input("Diameter of pizza 5: "))
        diam_of_pizza6 = 0

    if num_of_pizzas == 6:
        diam_of_pizza1 = float(input("Diameter of pizza 1: "))
        diam_of_pizza2 = float(input("Diameter of pizza 2: "))
        diam_of_pizza3 = float(input("Diameter of pizza 3: "))
        diam_of_pizza4 = float(input("Diameter of pizza 4: "))
        diam_of_pizza5 = float(input("Diameter of pizza 5: "))
        diam_of_pizza6 = float(input("Diameter of pizza 5: "))

    # creates the base cost of any pizza
    base_cost = constants.LABOUR_COST + constants.RENTAL_COST

    # ask user if they want their subtotal
    print_subtotal = input("Would you like your subtotal(y/n): ")

    # does the math to determine the cost of all their pizzas
    cost_of_pizza1 = float(constants.TOPPING_COST * diam_of_pizza1)
    cost_of_pizza2 = float(constants.TOPPING_COST * diam_of_pizza2)
    cost_of_pizza3 = float(constants.TOPPING_COST * diam_of_pizza3)
    cost_of_pizza4 = float(constants.TOPPING_COST * diam_of_pizza4)
    cost_of_pizza5 = float(constants.TOPPING_COST * diam_of_pizza5)
    cost_of_pizza6 = float(constants.TOPPING_COST * diam_of_pizza6)

    # calculates the cost of labour and rental depending on how many
    # pizzas you order
    base_cost_of_all_pizzas = base_cost * num_of_pizzas

    # determines the subtotal then formats it to have 2 decimal places
    subtotal = cost_of_pizza1 + cost_of_pizza2 + base_cost_of_all_pizzas + \
        cost_of_pizza3 + cost_of_pizza4 + cost_of_pizza5 + cost_of_pizza6
    subtotal2 = ("{:.2f}".format(subtotal))

    # determines the total then formats it to have 2 decimal places
    total = subtotal * 1.13
    total = ("{:.2f}".format(total))

    # if the user wants the subtotal this will print it to the user
    if print_subtotal == "y":
        print("Your subtotal is ${}".format(subtotal2))

    # prints the total cost to the screen
    print("Your total cost with HST is ${}".format(total))

    # asks user if they want to order more pizza
    new_order = input("would you like to make another order? (y/n): ")

    # if they do want more then it will restart the program
    if new_order == "y":
        order_pizza()


# does the inital startup of the program
if __name__ == "__main__":
    order_pizza()
