import os
from dotenv import load_dotenv

load_dotenv()

DEBUG = os.getenv("FASTAPI_DEBUG", "False").lower() == "true"
OPENAI_API_KEY = os.getenv("FASTAPI_OPENAI_API_KEY")

if DEBUG:
    print("Running in debug mode")
