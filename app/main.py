import streamlit as st
from utils import get_user_mood, get_weather_data, recommend_activities

# Set up the page configuration for Streamlit
st.set_page_config(page_title="AI Wellness Recommender")
st.title("🌿 Mood-Based Wellness Recommender")

# Collect user input using Streamlit UI components

# User name input (text input remains the same)
name = st.text_input("Enter your name")

# Age input (slider remains the same)
age = st.slider("Select your age", 10, 100, 25)

# Gender input (dropdown remains the same)
gender = st.selectbox("Select your gender", ["Male", "Female", "Other"])

# Pickup buttons for "Enter your city" - Indian Cities
indian_cities = [
    "New Delhi", "Mumbai", "Kolkata", "Bangalore", "Chennai", "Hyderabad",
    "Pune", "Jaipur", "Lucknow", "Ahmedabad", "Surat", "Kochi", "Goa", "Chandigarh"
]
city_choice = st.selectbox("Choose your city (for weather context)", indian_cities)

# Pickup buttons for "How are you feeling today?"
moods = ["Happy", "Sad", "Neutral", "Stressed", "Excited", "Tired"]
mood_choice = st.selectbox("How are you feeling today?", moods)

# Button to trigger the recommendation process
if st.button("Get Recommendations"):
    # Check if the user has selected city and mood
    if city_choice == "Other" or mood_choice == "Other":
        st.warning("Please select an option or fill in all fields to continue.")
    else:
        # Use the selected city to fetch weather data
        weather = get_weather_data(city_choice)

        # Use the selected mood to get the mood classification
        mood = get_user_mood(mood_choice)

        # Get personalized activity recommendations based on mood, weather, age, and gender
        recs = recommend_activities(mood, weather, age, gender)

        # Display the recommendations
        st.subheader(
            f"Hi {name}, based on your mood ({mood}) and weather in {city_choice}, here are your recommendations:")

        for r in recs:
            st.markdown(f"- {r}")
