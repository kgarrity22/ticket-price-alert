import logging
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from keys import SENDER_EMAIL, SENDER_PASSWORD

# generic email sending
def send_email(receiver_email, subject, body):
    # Create a MIMEText object to represent the email & add headers
    message = MIMEMultipart()
    message["From"] = SENDER_EMAIL
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    message.add_header('X-Priority', '1') # add priority

    # Connect to Gmail's SMTP server
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, receiver_email, message.as_string())
        
        # Close the SMTP session
        server.quit()

    logging.info(f"Email sent successfully to {receiver_email}")

