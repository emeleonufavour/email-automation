import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import time
import schedule
from email_validator import validate_email, EmailNotValidError
from dotenv import load_dotenv
from datetime import datetime, timedelta

load_dotenv()

sender_email = os.getenv('SENDER_EMAIL')
sender_password = os.getenv('SENDER_PASSWORD')

def validate_email_address(email: str):
    """Validates an email address

    Args:
        email (str): Email to validate

    Returns:
        _type_: Normalised email if valid
    """
    try:
        valid = validate_email(email)
        return valid.email
    except EmailNotValidError as e:
        print(f"Email is not valid: {e}")

def send_email(recipients: list[str], subject: str, body: str) -> None:
    """Establish a connection to Gmail server and construct an email

    Args:
        recipients (list[str]): Recipients to send an email to
        subject (str): Subject of the email
        body (str): Body of the email
    """
    for recipient in recipients:
        validated_recipient = validate_email_address(recipient)
        if not validated_recipient:
            print(f"Cannot send email to invalid address => {recipient}")
            return
    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = ", ".join(recipients)
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipients, message.as_string())
        server.quit()
        print("Emails sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def job() -> None:
    """Send email
    """
    recipients = ["emeleonufavour15@gmail.com"]
    subject = "Tech Fam Biweekly meeting"
    body = "Testing"
    send_email(recipients, subject, body)

# current_time = datetime.now()
# target_time = current_time + timedelta(minutes=2)
# target_time_str = target_time.strftime("%H:%M")

# Schedule to run every 2 weeks at 10:00 am
schedule.every(2).weeks.at("10:00").do(job)

print("Scheduler running. Press Ctrl+C to stop.")

while True:
    schedule.run_pending()
    time.sleep(1)
