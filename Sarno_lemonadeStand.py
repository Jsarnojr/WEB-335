# Filename: Sarno_lemonadeStand.py
# Folder: week_3

# lemonadeStand
# Author: Joseph Sarno
# Date: 08/30/2024
# Description: This program calculates the cost and profit of making lemonade.

# Function to calculate the total cost of making lemonade
def calculate_cost(lemons_cost, sugar_cost):
    """
    This function calculates the total cost of making lemonade.
    :param lemons_cost: Cost of lemons
    :param sugar_cost: Cost of sugar
    :return: Total cost (lemons + sugar)
    """
    total_cost = lemons_cost + sugar_cost
    return total_cost

# Function to calculate the profit from selling lemonade
def calculate_profit(lemons_cost, sugar_cost, selling_price):
    """
    This function calculates the profit from selling lemonade.
    :param lemons_cost: Cost of lemons
    :param sugar_cost: Cost of sugar
    :param selling_price: Selling price of the lemonade
    :return: Profit (selling price - total cost)
    """
    total_cost = calculate_cost(lemons_cost, sugar_cost)
    profit = selling_price - total_cost
    return profit

# Variables to test the functions
lemons_cost = 2.50  # Example cost of lemons
sugar_cost = 1.50   # Example cost of sugar
selling_price = 10.00  # Example selling price of lemonade

# Calculate the total cost using calculate_cost function
total_cost = calculate_cost(lemons_cost, sugar_cost)

# Build a string to show the total cost calculation
cost_output = f"Cost of lemons: ${lemons_cost} + Cost of sugar: ${sugar_cost} = Total cost: ${total_cost}"

# Print the total cost calculation
print(cost_output)

# Calculate the profit using calculate_profit function
profit = calculate_profit(lemons_cost, sugar_cost, selling_price)

# Build a string to show the profit calculation
profit_output = f"Selling price: ${selling_price} - Total cost: ${total_cost} = Profit: ${profit}"

# Print the profit calculation
print(profit_output)
