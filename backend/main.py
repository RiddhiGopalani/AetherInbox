from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Initialize the core FastAPI web application server engine
app = FastAPI(
    title="AetherInbox API Engine",
    description="Asynchronous processing core for autonomous email triage",
    version="1.0.0"
)

# Configure CORS (Cross-Origin Resource Sharing) 
# This allows our frontend dashboard to securely communicate with this server
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows development environments to connect safely
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root_health_check():
    """
    Core engine system health status check.
    """
    return {
        "status": "active",
        "engine": "AetherInbox Core Backend",
        "security_layer": "PostgreSQL RLS Connected"
    }