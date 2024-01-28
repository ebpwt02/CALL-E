from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
# Replace the placeholder with your Atlas connection string
uri = "mongodb+srv://ebrewer02:MDB$PWandT02@call-e.lfwnmrz.mongodb.net/?retryWrites=true&w=majority"
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