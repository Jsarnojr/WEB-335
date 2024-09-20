"""
Title: sarno_usersp1.py
Author: Joseph Sarno
Date: 09/20/2024
Description: Python program to connect to web335DB and perform database operations.
"""

# Import necessary packages
from pymongo import MongoClient

# Establish a connection to the MongoDB database
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Access the web335DB database
db = client['web335DB']

# Function to display all documents in the user's collection
def display_all_users():
    print("Displaying all users:")
    for user in db.users.find({}):  # Retrieve all documents from the users collection
        print(user)

# Function to display a document where employeeId is 1011
def find_user_by_employee_id(employee_id):
    print(f"Displaying user with employeeId: {employee_id}")
    user = db.users.find_one({"employeeId": employee_id})
    print(user)

# Function to display a document where the lastName is Mozart
def find_user_by_last_name(last_name):
    print(f"Displaying user with lastName: {last_name}")
    user = db.users.find_one({"lastName": last_name})
    print(user)

# Call the functions to display the results
if __name__ == "__main__":
    display_all_users()  # Display all users
    find_user_by_employee_id("1011")  # Display user with employeeId 1011
    find_user_by_last_name("Mozart")  # Display user with lastName Mozart
