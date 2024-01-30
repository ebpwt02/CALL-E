from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import config

# Connect to MongoDB
uri = config.MONGODB_URI
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["CALL-E"]
collection = db.Users

# Function to retrieve all users
def get_all_users():
    users = collection.find()
    for user in users:
        print(user)

# Function to retrieve a single user by email
def get_user_by_email(email):
    user = collection.find_one({"email": email})
    if user:
        print(user)
    else:
        print(f"No user found with email: {email}")

# Example Usage
print("All users:")
get_all_users()

print("\nUser with specific email:")
get_user_by_email("j.andrew.brewer@gmail.com")