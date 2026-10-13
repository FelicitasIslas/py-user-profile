from motor.motor_asyncio import AsyncIOMotorClient
from src.enviroment.load_enviroment import load_enviroment

env = load_enviroment()

MONGODB_URL = env["MONGODB_URL"]

def get_database_connection(collection: str) -> AsyncIOMotorClient:
    client = AsyncIOMotorClient(MONGODB_URL)
    return client.user_profile.get_collection(collection)