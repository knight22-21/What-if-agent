from dotenv import load_dotenv
import os

# Load from .env
load_dotenv()

# Retrieve token
HF_API_TOKEN = os.getenv("HF_API_TOKEN")

if not HF_API_TOKEN:
    raise ValueError("Hugging Face API token not found in .env file.")
