from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import config

# MongoDB connection setup
uri = config.MONGODB_URI
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["CALL-E"]
collection = db.Users

def add_user(name, email, phone, superuser):
    """
    Function to add a new user to the database.
    
    Parameters:
    name (str): Name of the user
    email (str): Email address of the user
    phone (str): Phone number of the user
    superuser (str): Whether the user is a superuser ("yes" or "no")
    """
# Check if a user with the given email already exists
    existing_user = collection.find_one({"email": email})
    if existing_user:
        print(f"Error: A user with the email {email} already exists.")
        return
    data = {
        "name": name, 
        "email": email,
        "phone": phone,
        "superuser": superuser
    }
    
    try:
        collection.insert_one(data)
        print(f"User {name} added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
add_user("Andy Brewer", "j.andrew.brewer@gmail.com", "7707784176", "no")