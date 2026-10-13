from dotenv import dotenv_values
import os

# load enviroment values

def load_enviroment():
    enviroment = os.getenv("ENVIRONMENT")
    env_file = f".env.{enviroment}"
    return dotenv_values(env_file)