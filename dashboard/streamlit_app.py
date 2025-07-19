import streamlit as st
import sys
import os
from datetime import datetime

# Adjust import paths
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from storage.database import get_all_threats, init_db, save_threat
from ingestion.twitter_fetcher import fetch_tweets_with_tweepy, fetch_tweets_with_tweepy_dummy
from preprocessing.clean_text import clean_text
from detection.classifier import detect_threat
from alerts.email_alert import send_email_alert

# Initialize the database
init_db()

# Streamlit App UI
st.title("🚨 Social Media Threat Monitor")

# Input form for user query
with st.form(key="search_form"):
    query = st.text_input("Enter search query:", value="protest")
    max_results = st.slider("Max tweets to fetch", min_value=10, max_value=100, value=20, step=10)
    use_dummy = st.checkbox("Use dummy data instead of live tweets", value=True)
    submit_button = st.form_submit_button("🔍 Search and Detect Threats")

# If form is submitted
if submit_button:
    with st.spinner("Fetching tweets and detecting threats..."):
        try:
            # Choose between dummy or live data
            if use_dummy:
                posts = fetch_tweets_with_tweepy_dummy(query=query, max_results=max_results)
            else:
                posts = fetch_tweets_with_tweepy(query=query, max_results=max_results)

            threats_found = 0

            for post in posts:
                cleaned = clean_text(post["content"] if isinstance(post, dict) else post)
                threats = detect_threat(cleaned)

                if threats:
                    threats_found += 1
                    for label, score in threats:
                        save_threat(post, label, score)
                    send_email_alert(post, threats)

            st.success(f"Detection complete. {threats_found} threat(s) found.")
        except Exception as e:
            st.error(f"An error occurred: {e}")

# Show detected threats from database
rows = get_all_threats()
st.header("📌 Detected Threats")

if not rows:
    st.warning("No threats detected yet.")
else:
    for row in rows:
        try:
            confidence = round(float(row[5]), 2)
        except:
            confidence = "N/A"

        st.markdown(f"""
        - **Platform:** {row[1]}
        - **User:** {row[2]}
        - **Threat:** `{row[4]}` (**{confidence}**)
        - **Content:** {row[3]}
        - [Open Post]({row[6]})
        - _Time_: {row[7]}
        ---
        """)
