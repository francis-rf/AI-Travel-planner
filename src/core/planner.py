from langchain_core.messages import HumanMessage, AIMessage
from src.chains.itinerary_chain import generate_itinerary   
from utils.logger import get_logger
from utils.custom_exception import CustomException

logger = get_logger(__name__)

class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.itinerary = ""  

        logger.info("TravelPlanner initialized")

    def set_city(self, city: str):
        if not city or not city.strip():
            raise ValueError("City cannot be empty")
        
        self.city = city.strip()
        self.messages.append(HumanMessage(content=f"City: {self.city}"))
        logger.info(f"City set to {self.city}")
    
    def set_interests(self, interest_str: str):
        if not interest_str or not interest_str.strip():
            raise ValueError("Interests cannot be empty")
        
        self.interests = [i.strip() for i in interest_str.split(',') if i.strip()]
        self.messages.append(HumanMessage(content=f"Interests: {', '.join(self.interests)}"))
        logger.info(f"Interests set to {self.interests}")

    def generate_itinerary(self):
        try:
            # Call the function with correct parameters
            self.itinerary = generate_itinerary(self.city, self.interests)
            self.messages.append(AIMessage(content=self.itinerary))
            logger.info("Itinerary generated successfully")
            return self.itinerary
        except Exception as e:
            logger.error(f"Failed to generate itinerary: {e}")
            raise CustomException("Failed to generate itinerary", e)