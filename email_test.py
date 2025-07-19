from alerts.email_alert import send_email_alert  # adjust if your file is named differently

sample_post = {
    "platform": "Twitter",
    "username": "user123",
    "content": "I will bomb the place tonight!",
    "url": "https://twitter.com/user123/status/123456789"
}

sample_threats = [("terrorism", 0.91), ("violence", 0.88)]

send_email_alert(sample_post, sample_threats)
print("✅ Email sent (if credentials are correct).")
