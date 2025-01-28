
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By

from send_email import send_email
from keys import RECEIVER_EMAIL
from send_sms import send_text

# CONSTANTS
STUBHUB_URL = "https://www.stubhub.com/big-east-basketball-tournament-new-york-tickets-3-15-2025/event/154773723/?qid=45d39957b59c4a1f049e0c527d6382ba&iid=0e0336c9-3d42-4dfb-a365-0ed277475647&index=stubhub&ut=1c09179ef2a3b28e81530ebab681e57503c0b578&quantity=3"
TICKET_X_PATHS = {
    "ticket_price": '//*[@id="listings-container"]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]', # ticket price
    "ticket_rating": '//*[@id="listings-container"]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]' # rating of the tickets
}
EMAIL_SUB = "Ticket Prices for the Big East Championship Have Dropped"
PRICE_THRESHOLD = 80


# general function for retrieving ticket info 
## should work for any ticketing site and any page element
def get_ticket_info(url, xPaths):
    data = {}
    #open up chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run headless Chrome. comment out to see the browser actually open.

    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # find the xPath values
    for key, element in xPaths.items():
        try:
            retrieved = driver.find_element(By.XPATH, element)
            data[key] = retrieved.get_attribute('innerHTML')
        except Exception as e:
            logging.error(f"Error finding element {key}: {e}")
        
    driver.quit()
    
    if len(data.keys()):
        if int(data['ticket_price'].replace("$", "")) <= PRICE_THRESHOLD:
            notify_price_drop(data)
    


# Send notification email if ticket price is below price target
def notify_price_drop(ticketInfo):
    global email_sent  

    subject = EMAIL_SUB
    body = f"Big East Championship ticket prices have dropped below ${PRICE_THRESHOLD}. The available tickets are now selling at {ticketInfo['ticket_price']} with a stubhub rating of {ticketInfo['ticket_rating']}. Get them now here: {STUBHUB_URL}!"

    try:
        send_email(RECEIVER_EMAIL, subject, body)
        email_sent = True  # Set flag to true after email is sent

    except Exception as e:
        logging.error(f"Failed to send notification email: {e}")



get_ticket_info(STUBHUB_URL, TICKET_X_PATHS)