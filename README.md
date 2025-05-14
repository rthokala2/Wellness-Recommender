 AI Mood-Based Wellness Recommender
This project is an AI-powered wellness assistant that provides personalized wellness activity recommendations based on the user's mood, location (weather), age, and gender.

Built using Streamlit, it combines NLP sentiment analysis, live weather data, and rule-based logic to suggest mood-lifting activities.

🚀 Features
🔍 Mood Detection using VADER or Transformers (e.g., bert-base-uncased)

☁️ Weather-aware Suggestions using OpenWeatherMap API

🧠 Contextual Recommendations based on mood, weather, age, and gender

🇮🇳 Pre-set Indian City Selection

🎯 Easy-to-use UI with radio buttons and dropdowns

🛠️ Installation
Clone the repository

bash
Copy
Edit
git clone https://github.com/your-username/wellness-recommender.git
cd wellness-recommender
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Set your OpenWeatherMap API key

Edit utils.py and replace the placeholder:

python
Copy
Edit
api_key = "YOUR_API_KEY"
🧪 Run the App
bash
Copy
Edit
streamlit run app/main.py
📸 Screenshots
Input	Output

🧩 File Structure
bash
Copy
Edit
wellness-recommender/
│
├── app/
│   ├── main.py               # Streamlit frontend
│   └── utils.py              # Mood analysis, weather fetching, and recommendation logic
│
├── requirements.txt
└── README.md
📈 Recommendation Logic
The system combines:

Sentiment classification → "Happy", "Sad", "Neutral", etc.

Weather condition → "Rainy", "Sunny", "Cold", etc.

Demographic factors → Age & Gender

Activity rules → Tailored suggestions (e.g., yoga, journaling, walking, social call)

Example:
A sad 55-year-old woman on a rainy day might get suggestions like:

"Try a 10-minute guided meditation"

"Call a loved one"

"Cozy up with a warm beverage and book"

🧠 Future Enhancements
Integrate mood prediction using BERT (transformers)

Store user history & track emotional trends

Add voice input and mobile support

Personalized chatbot integration (e.g., with LangChain)

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first.

