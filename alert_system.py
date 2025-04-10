# alert_system.py
import smtplib
from email.message import EmailMessage

def send_alert_email(emotion):
    msg = EmailMessage()
    msg.set_content(f"Alert: The user seems to be feeling {emotion}. Please check on them.")
    msg['Subject'] = "Emotion Alert from EmotiCare"
    msg['From'] = "harshanaaramesh@gmail.com"
    msg['To'] = "harshanaa.c.r.it26@psvpec.in"  # ✅ Changed recipient here

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("harshanaaramesh@gmail.com", "tjrc qiuk jzwa ykal")
            smtp.send_message(msg)
        print("Alert email sent!")
    except Exception as e:
        print("Failed to send email:", e)
 