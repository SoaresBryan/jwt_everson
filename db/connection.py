from motor.motor_asyncio import AsyncIOMotorClient

MONGO_DB_URL = "mongodb://localhost:27017"

client = AsyncIOMotorClient(MONGO_DB_URL)

db = client["Spike_autenticacao"] 
