import smtplib
from email.mime.text import MIMEText
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from project_config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_email_alert(post, threats):
    msg = MIMEText(f"""🚨 Threat Detected!

Platform: {post['platform']}
User: {post['username']}
Content: {post['content']}
URL: {post['url']}
Threats: {threats}
    """)
    msg["Subject"] = "Threat Alert Detected"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
