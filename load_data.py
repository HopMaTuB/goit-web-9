import mongoengine as me
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import json

uri = "mongodb+srv://sunkiper:04101993Qwe@cluster1.7bztefj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster1"

client = MongoClient(uri, server_api=ServerApi('1'))
me.connect(host=uri)
db = client["sunkiper"]

with open('authors.json', 'r') as authors_file:
    authors_data = json.load(authors_file)
authors_collection = db['authors']
if isinstance(authors_data, list):
    authors_collection.insert_many(authors_data)
else:
    authors_collection.insert_one(authors_data)


with open('quotes.json', 'r') as quotes_file:
    quotes_data = json.load(quotes_file)
quotes_collection = db['quotes']
if isinstance(quotes_data, list):
    quotes_collection.insert_many(quotes_data)
else:
    quotes_collection.insert_one(quotes_data)