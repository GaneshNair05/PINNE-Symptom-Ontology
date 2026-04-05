import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

load_dotenv()
# Get the URI from your .env file
MONGO_URI = os.getenv("MONGODB_URL")
# Initialize the Asynchronous client
client = AsyncIOMotorClient(MONGO_URI)
# Select the database
db = client["pinne_db"]
ontology_collection = db["ontology"]