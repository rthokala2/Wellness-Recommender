import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import random

analyzer = SentimentIntensityAnalyzer()

# Helper function to analyze the user's mood based on input text
def get_user_mood(text):
    """
    Analyzes user text and classifies mood as happy, sad, angry, anxious, or neutral.
    """
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.5:
        return "happy"
    elif score <= -0.5:
        return "sad"
    elif "angry" in text.lower():
        return "angry"
    elif "anxious" in text.lower() or "nervous" in text.lower():
        return "anxious"
    else:
        return "neutral"

# Function to fetch current weather from OpenWeatherMap API
def get_weather_data(city):
    """
    Fetches current weather using OpenWeatherMap API and categorizes it.
    """
    try:
        api_key = "b9cbce5f5be27f6731b1973338324740"  # Your OpenWeatherMap API key
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_desc = data['weather'][0]['main'].lower()
            if "rain" in weather_desc:
                return "rainy"
            elif "clear" in weather_desc:
                return "sunny"
            elif "cloud" in weather_desc:
                return "cloudy"
            elif "snow" in weather_desc:
                return "cold"
            else:
                return "moderate"
        else:
            return "moderate"
    except Exception as e:
        print(f"Error fetching weather data: {e}")
        return "moderate"

# Heavy recommendations based on mood, weather, age, and gender
def recommend_activities(mood, weather, age, gender):
    """
    Generates personalized wellness activity suggestions based on mood, weather, age, and gender.
    """
    activities = []

    # Mood-based suggestions
    mood_activities = {
        "happy": [
            "Dance to your favorite upbeat song!",
            "Try a fun recipe or invite a friend for tea.",
            "Take a short trip to a new place you haven't explored.",
            "Start a new creative project like painting or writing.",
            "Engage in physical activity like cycling or yoga."
        ],
        "sad": [
            "Try a 10-minute guided meditation.",
            "Take a short walk and get some fresh air.",
            "Watch a feel-good movie or read an inspiring book.",
            "Write down your thoughts and emotions in a journal.",
            "Talk to a close friend or family member."
        ],
        "angry": [
            "Take deep breaths and practice calming techniques.",
            "Go for a run or do a high-intensity workout to release frustration.",
            "Try some yoga or tai chi to calm your nerves.",
            "Engage in an activity that requires focus, like puzzles or painting.",
            "Journal about what triggered your anger and how to manage it."
        ],
        "anxious": [
            "Practice mindfulness or deep breathing exercises.",
            "Try some light stretching or yoga.",
            "Listen to calming music or a guided meditation.",
            "Organize your space or start a small creative project.",
            "Talk to a therapist or support group if you need someone to listen."
        ],
        "neutral": [
            "Write in your journal for 5 minutes.",
            "Read or listen to a calming podcast.",
            "Go for a walk and clear your mind.",
            "Try a new hobby or practice a skill you've been meaning to learn.",
            "Watch something that inspires you or makes you think."
        ]
    }

    activities.extend(mood_activities.get(mood, []))

    # Weather-based suggestions
    weather_activities = {
        "sunny": [
            "Go for a light jog or walk outside.",
            "Take a picnic in the park or visit a nearby botanical garden.",
            "Try outdoor photography or sketching.",
            "Engage in outdoor sports like tennis, cycling, or running."
        ],
        "rainy": [
            "Cozy up indoors with a book and tea.",
            "Try baking a new recipe or cooking something you've never made before.",
            "Do an indoor workout or dance to your favorite tunes.",
            "Watch a documentary or binge-watch your favorite series."
        ],
        "cold": [
            "Do some indoor yoga or stretching.",
            "Have a cozy indoor movie marathon with blankets and tea.",
            "Try a warm, comforting hobby like knitting or crafting.",
            "Bake some homemade bread or cookies."
        ],
        "cloudy": [
            "Try painting or indoor hobbies.",
            "Take a nap and relax your mind.",
            "Meditate or listen to a mindfulness podcast.",
            "Plan a short-term project or organize your workspace."
        ],
        "moderate": [
            "Go for a walk, take in the fresh air.",
            "Do a light stretching session or yoga.",
            "Have a friend over for tea or a relaxed conversation.",
            "Try a hobby you've been wanting to start."
        ]
    }

    activities.extend(weather_activities.get(weather, []))

    # Age-based suggestions
    if age < 25:
        activities.append("Try a fun mobile wellness game or challenge.")
        activities.append("Join an online fitness challenge with friends.")
    elif age > 50:
        activities.append("Join a low-impact home fitness video.")
        activities.append("Try tai chi or walking meditation.")
    else:
        activities.append("Experiment with a new hobby or recipe.")
        activities.append("Take a break and try some self-care techniques.")

    # Gender and mood personalization
    if gender == "Female" and mood == "sad":
        activities.append("Connect with a close friend or family member over a call.")
        activities.append("Indulge in a relaxing bath with calming scents.")
    elif gender == "Male" and mood == "happy":
        activities.append("Consider a group activity like a sports game or volunteering.")
        activities.append("Try a physical challenge like rock climbing or hiking.")
    elif gender == "Other" and mood == "neutral":
        activities.append("Explore creative self-expression like art or music.")
        activities.append("Practice mindfulness or meditation to relax your mind.")

    # Add some random uplifting suggestions
    uplifting_activities = [
        "Try something completely new today, like learning a language or cooking a new dish.",
        "Help someone else by doing a random act of kindness.",
        "Set a small, achievable goal today and feel the satisfaction of accomplishment.",
        "Find something beautiful in nature and take a moment to appreciate it.",
        "Learn something new, like a dance move or a musical instrument!"
    ]
    activities.append(random.choice(uplifting_activities))

    return activities
