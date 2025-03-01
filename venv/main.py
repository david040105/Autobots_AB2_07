from pymongo import MongoClient
from getpass import getpass

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")  # Replace with your MongoDB connection string
db = client["dskjv"]  # Replace with your database name
users_collection = db["users"]  # Replace with your collection name

# Function to validate user login
def login():
    # Get user input for username and password
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    # Find the user by username
    user = users_collection.find_one({"username": username})

    if user:
        # If user exists, check if the password matches
        if user["password"] == password:
            print("Login successful!")
        else:
            print("Invalid password!")
    else:
        print("Username not found!")

# Basic registration function for new users
def register():
    username = input("Enter username: ")
    password = getpass("Enter password: ")

    # Check if the username already exists
    existing_user = users_collection.find_one({"username": username})

    if existing_user:
        print("Username already taken!")
    else:
        # Insert the new user into the collection
        users_collection.insert_one({"username": username, "password": password})
        print("User registered successfully!")

# Main function to handle login or registration
def main():
    action = input("Do you want to (L)ogin or (R)egister? ").lower()

    if action == "l":
        login()
    elif action == "r":
        register()
    else:
        print("Invalid option!")

if __name__ == "__main__":
    main()
