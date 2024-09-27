# File: yourLastName_usersp2.py
# Folder: week_7
# Author: Joseph Sarno
# Date: 09/27/2024
# Description: This script connects to the web335DB database, creates a user document,
# updates the email field, and deletes the document, printing the results at each step.

from pymongo import MongoClient

# Step 2: Connect to MongoDB
client = MongoClient('mongodb+srv://<username>:<password>@cluster0.mongodb.net/web335DB')
db = client.web335DB
users_collection = db.users

# Step 3: Create a new user document
new_user = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "johndoe@example.com",
    "employee_id": "1010"
}

# Insert the document into the 'users' collection
new_user_id = users_collection.insert_one(new_user).inserted_id
print(f"New user document created with ID: {new_user_id}")

# Step 4: Prove the document was created
created_user = users_collection.find_one({"_id": new_user_id})
print("Document after creation:", created_user)

# Step 5: Update the email address of the document
users_collection.update_one(
    {"_id": new_user_id},
    {"$set": {"email": "john.doe.updated@example.com"}}
)

# Step 6: Prove the document was updated
updated_user = users_collection.find_one({"_id": new_user_id})
print("Document after email update:", updated_user)

# Step 7: Delete the document
users_collection.delete_one({"_id": new_user_id})
print(f"User document with ID: {new_user_id} has been deleted.")

# Step 8: Prove the document was deleted
deleted_user = users_collection.find_one({"_id": new_user_id})
print("Document after deletion:", deleted_user)  # This should print None if the deletion was successful.
