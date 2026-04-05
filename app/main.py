from fastapi import FastAPI
from dotenv import load_dotenv
from app.api import emergencies 
from app.core.db import client
import os 

load_dotenv()
app = FastAPI(
    title="Symptom System",
    description="Probablistic Intelligent Network for Symptom Ontology"
)
app.include_router(emergencies.router, prefix="/api/emergencies", tags=["Emergencies"])

@app.get("/")
async def root():
    return{
        "message" : "Server is online"
    }
@app.on_event("startup")
async def startup_event():
    print("Attempting to connect to MongoDB...")
    try:
        # Ping the database using the client we imported from db.py
        await client.admin.command('ping')
        print("✅ Successfully connected to MongoDB!")
    except Exception as e:
        print(f"❌ Failed to connect to MongoDB.")
        print(f"Error details: {e}")

@app.on_event("shutdown")
async def shutdown_event():
    print("Shutting down")