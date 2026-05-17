import os
from dotenv import load_dotenv
from supabase import create_client, Client

# Read the keys out of our hidden .env file
load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

# Check to ensure keys are actually loading properly
if not url or not key:
    raise ValueError("Error: Could not find SUPABASE_URL or SUPABASE_KEY in environment.")

# Initialize the official cloud communication connection
supabase: Client = create_client(url, key)
print("Supabase cloud database connection client initialized successfully!")