# 🔍 Social Media Monitoring and Threat Detection System

This project is a real-time social media monitoring tool that fetches live tweets from Twitter using the Tweepy API and applies a trained NLP-based threat detection model to identify potentially harmful or suspicious content.

🚀 Features
🔎 Real-time Tweet Fetching
Retrieves recent tweets based on a keyword or hashtag using the Twitter API.
🧠 Threat Detection Model
Uses an AI/ML model to classify tweets into various risk categories, including potential threats, protests, and safe content.
📊 Confidence Scoring
Each tweet is evaluated with a confidence score to reflect prediction certainty.
🌐 Platform-Agnostic Structure
Easily extendable to other platforms like Reddit, Instagram, or news feeds.
📦 Dummy & Live Modes
Test with predefined dummy tweets or switch to live tweet fetching with just a function call.
🛠️ Tech Stack
Python
Tweepy (Twitter API)
Sklearn / NLP pipeline for classification
Pandas, datetime for data processing
Streamlit (Optional for UI)
📌 Use Cases
Threat intelligence and security monitoring
Protest and sentiment analysis
Social media surveillance for law enforcement
Real-time event detection and alerting
