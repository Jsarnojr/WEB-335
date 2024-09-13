"""
Author: Joseph Sarno
Date: September 13, 2024
File Name: Sarno_lemonadeStandSchedule.py
Description: This file manages a weekly schedule for a lemonade stand using lists, loops, and conditionals.
"""

# List of tasks related to running a lemonade stand
tasks = ["Buy lemons", "Make lemonade", "Sell lemonade", "Count earnings", "Clean up"]

# Printing all tasks using a for loop
print("Tasks for running the lemonade stand:")
for task in tasks:
    print(task)

# List of days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Using a for loop to iterate over the days and assign tasks to each weekday
print("\nWeekly Schedule:")
for i, day in enumerate(days):
    if day == "Saturday" or day == "Sunday":  # Weekend days
        print(f"{day}: It's a day off! Time to rest.")
    else:  # Assign tasks to weekdays
        print(f"{day}: Today's task is to {tasks[i % len(tasks)]}.")
