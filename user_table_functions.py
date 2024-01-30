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




def update_user(current_email, new_email=None, name=None, phone=None):
    """
    Function to update user details including email.

    Parameters:
    current_email (str): Current email address of the user to identify them.
    new_email (str, optional): New email address of the user.
    name (str, optional): New name of the user.
    phone (str, optional): New phone number of the user.
    """
    update_data = {}
    if new_email:
        # Check if the new email is already in use
        if collection.find_one({"email": new_email}):
            print(f"Error: The email {new_email} is already in use.")
            return
        update_data['email'] = new_email
    if name:
        update_data['name'] = name
    if phone:
        update_data['phone'] = phone

    if not update_data:
        print("No update information provided.")
        return

    try:
        result = collection.update_one({"email": current_email}, {"$set": update_data})
        if result.matched_count > 0:
            print(f"User with email {current_email} updated successfully.")
        else:
            print(f"No user found with current email: {current_email}")
    except Exception as e:
        print(f"An error occurred: {e}")


def delete_user_by_email(email):
    """
    Function to delete a user from the database based on their email address.

    Parameters:
    email (str): Email address of the user to be deleted.
    """
    try:
        result = collection.delete_one({"email": email})
        if result.deleted_count > 0:
            print(f"User with email {email} has been deleted.")
        else:
            print(f"No user found with email: {email}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage Delete
#delete_user_by_email("j.andrew.brewer@gmail.com")

# Example usage Update
# update_user("j.andrew.brewer@gmail.com", new_email="andrew.brewer@example.com", name="Andrew Brewer", phone="1234567890")


# Example Usage Read
#print("All users:")
#get_all_users()
#print("\nUser with specific email:")
#get_user_by_email("j.andrew.brewer@gmail.com")


# Example usage Add
#add_user("Andy Brewer", "j.andrew.brewer@gmail.com", "7707784176", "no")