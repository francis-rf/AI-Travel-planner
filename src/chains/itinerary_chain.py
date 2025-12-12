import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from config.config import GROQ_API_KEY
from utils.logger import get_logger
from utils.custom_exception import CustomException

# Load env variables
load_dotenv(override=True)

logger = get_logger(__name__)

# Define prompt template
itinerary_prompt = ChatPromptTemplate.from_messages([
    ('system', """You are an expert local travel guide and itinerary planner. 
    Your goal is to create a perfectly personalized one-day itinerary for {city} based on the user's specific interests: {interests}.

    Your response must be strictly formatted as follows:
    
    ### 🏙️ Top 5 Recommended Places in {city}
    List exactly 5 places that best match the provided interests. For each place, briefly explain *why* it aligns with the user's preference.

    ### 📅 Day Trip Itinerary
    Create a chronological schedule (Morning, Afternoon, Evening) incorporating these places.
    - **Morning**: [Activities]
    - **Afternoon**: [Activities]
    - **Evening**: [Activities]
    
    ### 💡 Pro Tips
    Include 2-3 practical tips for this specific trip (e.g., best transport, hidden gems, or food recommendations).

    Keep the tone enthusiastic, professional, and concise. Use Markdown formatting."""),
    ('human', 'Create an itinerary for my day trip to {city} involving {interests}')
])

def generate_itinerary(city: str, interests: list[str]) -> str:
    # Input validation
    if not city or not city.strip():
        raise ValueError("City cannot be empty")
    if not interests:
        raise ValueError("At least one interest must be provided")
    
    try:
        logger.info(f'Generating itinerary for {city} with interests: {interests}')
        
        # Initialize LLM
        # Using environment variable for model with a fallback
        llm = ChatGroq(
            api_key=GROQ_API_KEY,
            model=os.getenv('OPENAI_MODEL', 'qwen/qwen3-32b'), 
        )
        
        # Create Chain: Prompt -> LLM -> Output Parser
        chain = itinerary_prompt | llm | StrOutputParser()
        
        result = chain.invoke({
            "city": city.strip(), 
            "interests": ", ".join(interests)
        })
        
        logger.info('Itinerary generated successfully.')
        return result

    except Exception as e:
        logger.error(f"Error generating itinerary for {city}: {str(e)}")
        raise CustomException("Failed to generate itinerary", e)