from twilio.rest import Client
from keys import TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN, TWILIO_NUMBER, CELL_NUMBER

def send_text(body, recipient=CELL_NUMBER):
    client = Client(TWILIO_ACCOUNT_ID, TWILIO_AUTH_TOKEN)

    client.messages.create(
        to=recipient,
        from_=TWILIO_NUMBER,
        body=body)
    
    print("Message sent!")
    



