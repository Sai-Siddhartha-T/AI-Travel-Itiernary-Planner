import streamlit as st
from dotenv import load_dotenv

from src.core.planner import TravelPlanner

load_dotenv()

st.set_page_config(page_title="AI Travel Planner", page_icon=":airplane:", layout="wide")
st.title("AI Travel Itinerary Planner")
st.write(
    "Plan your perfect day trip with the help of AI! Enter your destination and interests, and let the AI create a personalized itinerary for you."
)


with st.form("planner_form"):
    city = st.text_input("Enter your destination city")
    interests = st.text_input("Enter your interests (comma-separated)")
    submitted = st.form_submit_button("Generate Itinerary")

    if submitted:
        if city.strip() and interests.strip():
            planner = TravelPlanner()
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary = planner.create_iternary()

            st.subheader("Your Personalized Itinerary")
            st.markdown(itinerary)
        else:
            st.error("Please enter both city and interests to generate an itinerary.")

