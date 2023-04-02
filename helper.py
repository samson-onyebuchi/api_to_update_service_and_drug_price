import pymongo
from pymongo import MongoClient
from mongodb_url import mongoDB_url

# Set up the MongoDB Atlas connection string
# Replace <username>, <password>, and <cluster> with your own values
client = pymongo.MongoClient(mongoDB_url())

# Select the database and collection you want to search

db = client["mydatabase"]
collection = db["practice"]

# Define the data you want to check for
#query = {"phone": 2348035756148}

#query = int(input("Enter phone"))
# Check if the data exists in the collection
    # if collection.find_one(query) is not None:
    #     print("Data exists in the collection.")
    # else:
    #     print("Data does not exist in the collection.")
class Database_usage:
    
    def check_if_user_exist(phone):
        #phone = self.phone
        if collection.find_one({"phone":phone}) is not None:
            return("Data exists in the collection.")
        else:
            return("Data does not exist in the collection.")
        
#Database_usage.check_if_user_exist(2348035756148)