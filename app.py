from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field
from typing import List

from src.core.planner import TravelPlanner
from utils.logger import get_logger
from utils.custom_exception import CustomException

# Initialize logger
logger = get_logger(__name__)

# Create FastAPI app
app = FastAPI(
    title="AI Travel Planner API",
    description="Generate personalized day trip itineraries using AI",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic models
class ItineraryRequest(BaseModel):
    city: str = Field(..., min_length=1, description="City name for the trip")
    interests: List[str] = Field(..., min_items=1, description="List of user interests")

class ItineraryResponse(BaseModel):
    itinerary: str
    city: str
    interests: List[str]

@app.post("/api/generate-itinerary", response_model=ItineraryResponse)
async def generate_itinerary_endpoint(request: ItineraryRequest):
    """Generate a travel itinerary based on city and interests"""
    try:
        logger.info(f"Received request for city: {request.city}, interests: {request.interests}")
        
        # Initialize planner
        planner = TravelPlanner()
        
        # Set city and interests
        planner.set_city(request.city)
        planner.set_interests(", ".join(request.interests))
        
        # Generate itinerary
        itinerary = planner.generate_itinerary()
        
        logger.info("Itinerary generated successfully")
        
        return ItineraryResponse(
            itinerary=itinerary,
            city=request.city,
            interests=request.interests
        )
        
    except ValueError as e:
        logger.error(f"Validation error: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except CustomException as e:
        logger.error(f"Custom exception: {str(e)}")
        raise HTTPException(status_code=500, detail="Failed to generate itinerary. Please try again.")
    except Exception as e:
        logger.error(f"Unexpected error: {str(e)}")
        raise HTTPException(status_code=500, detail="An unexpected error occurred.")

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {"status": "healthy", "service": "AI Travel Planner"}

# Mount static files LAST - this catches all remaining routes
# The html=True parameter allows serving index.html at the root
app.mount("/", StaticFiles(directory="static", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    logger.info("Starting AI Travel Planner server...")
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
