from ingestion.twitter_fetcher import fetch_tweets_with_tweepy
from preprocessing.clean_text import clean_text
from detection.classifier import detect_threat
from alerts.email_alert import send_email_alert
from storage.database import init_db, save_threat

def run_pipeline():
    init_db()
    posts = fetch_tweets_with_tweepy()
    for post in posts:
        cleaned = clean_text(post["content"])
        threats = detect_threat(cleaned)
        if threats:
            for label, score in threats:
                save_threat(post, label, score)
            send_email_alert(post, threats)

if __name__ == "__main__":
    run_pipeline()
