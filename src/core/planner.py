from langchain_core.messages import HumanMessage, AIMessage

from src.chains.iternary_chain import generate_iternary, generate_itinerary
from src.utils.custom_exception import CustomException
from src.utils.logger import get_logger

logger = get_logger(__name__)


class TravelPlanner:
    def __init__(self):
        self.messages = []
        self.city = ""
        self.interests = []
        self.iternary = ""

        logger.info("Initialised TravelPlanner instance")

    def set_city(self, city: str):
        try:
            self.city = city.strip()
            self.messages.append(HumanMessage(content=self.city))
            logger.info(f"City set to: {self.city}")
        except Exception as e:
            logger.error(f"Error in set_city: {e}")
            raise CustomException("Failed to set city", e)

    def set_interests(self, interests_str: str):
        try:
            self.interests = [
                interest.strip() for interest in interests_str.split(",") if interest.strip()
            ]
            self.messages.append(HumanMessage(content=interests_str))
            logger.info(f"Interests set to: {self.interests}")
        except Exception as e:
            logger.error(f"Error in set_interests: {e}")
            raise CustomException("Failed to set interests", e)

    def create_iternary(self):
        try:
            logger.info(f"Generating itinerary for {self.city} with interests: {self.interests}")
            itinerary = generate_iternary(self.city, self.interests)
            self.iternary = itinerary
            self.messages.append(AIMessage(content=itinerary))
            logger.info("Itinerary generated successfully")
            return itinerary
        except Exception as e:
            logger.error(f"Error in create_iternary: {e}")
            raise CustomException("Failed to create itinerary", e)

    def create_itinerary(self):
        return self.create_iternary()
