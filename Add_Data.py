from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import config

# Replace the placeholder with your Atlas connection string
uri = config.MONGODB_URI
# Set the Stable API version when creating a new client
client = MongoClient(uri, server_api=ServerApi('1'))
                          
# Send a ping to confirm a successful connection
db = client["CALL-E"]
collection = db.Users

# Data to insert
data = {"name": "Andy Brewer", 
        "email": "j.andrew.brewer@gmail.com",
        "phone": "7707784176",
        "superuser": "no"}


# Insert data into the collection
collection.insert_one(data)
print("Data inserted successfully.")