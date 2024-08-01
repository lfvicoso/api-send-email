
import smtplib
from email.mime.text import MIMEText
from config import Config

def send_email(to, subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = Config.EMAIL_HOST_USER
    msg['To'] = to

    with smtplib.SMTP(Config.EMAIL_HOST, Config.EMAIL_PORT) as server:
        server.starttls()
        server.login(Config.EMAIL_HOST_USER, Config.EMAIL_HOST_PASSWORD)
        server.sendmail(Config.EMAIL_HOST_USER, to, msg.as_string())
