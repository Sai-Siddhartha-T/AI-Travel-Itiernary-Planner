from typing import Sequence

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

from src.config.config import get_groq_api_key


iternary_prompt = ChatPromptTemplate([
    (
        "system",
        "You are a helpful assistant. Create a day trip itinerary for {city} based on the user's interests: {interests}. Provide a brief, bulleted itinerary.",
    ),
    (
        "human",
        "Create an itinerary for my day trip, including places to visit, time to spend at each place, and the budget required. The city is {city} and my interests are {interests}.",
    ),
])


def get_llm() -> ChatGroq:
    api_key = get_groq_api_key()
    if not api_key:
        raise ValueError(
            "GROQ_API_KEY is missing. Add it to your environment or a .env file before generating an itinerary."
        )
    return ChatGroq(
        api_key=api_key,
        model="qwen/qwen3.8-27b",
        temperature=0.3,
    )


def generate_iternary(city: str, interests: Sequence[str]) -> str:
    cleaned_city = city.strip() if isinstance(city, str) else ""
    cleaned_interests = [
        interest.strip() for interest in interests if isinstance(interest, str) and interest.strip()
    ]

    if not cleaned_city:
        raise ValueError("City is required to generate an itinerary.")
    if not cleaned_interests:
        raise ValueError("At least one interest is required to generate an itinerary.")

    llm = get_llm()
    response = llm.invoke(
        iternary_prompt.format_messages(
            city=cleaned_city,
            interests=", ".join(cleaned_interests),
        )
    )
    return response.content.strip() if isinstance(response.content, str) else str(response.content)


def generate_itinerary(city: str, interests: Sequence[str]) -> str:
    return generate_iternary(city, interests)

 