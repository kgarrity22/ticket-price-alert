
from selenium import webdriver
from selenium.webdriver.common.by import By

# CONSTANTS
STUBHUB_URL = "https://www.stubhub.com/big-east-basketball-tournament-new-york-tickets-3-15-2025/event/154773723/?qid=45d39957b59c4a1f049e0c527d6382ba&iid=0e0336c9-3d42-4dfb-a365-0ed277475647&index=stubhub&ut=1c09179ef2a3b28e81530ebab681e57503c0b578&quantity=3"

TICKET_X_PATHS = {
    "ticket_price": '//*[@id="listings-container"]/div[1]/div/div[2]/div/div[1]/div[2]/div[1]', # ticket price
    "ticket_rating": '//*[@id="listings-container"]/div[1]/div/div[2]/div/div[1]/div[2]/div[2]/div/div/div/div[1]' # rating of the tickets
}


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
        retrieved = driver.find_element(By.XPATH, element)
        data[key] = retrieved.get_attribute('innerHTML')
    
    driver.quit()
    print('DATA: ', data)
    


def notify_price_drop():
    print("a new func")


# Function send_email_notification(spots, date, url):
#     For each phone number
#         Send a text with the link to buy

# Function main(args):
#     Schedule the permit check to run periodically

#     While True:
#         Run scheduled permit check
#         Wait for a short time to not overwork computer
#         If an email was sent:
#             Exit the loop

# if __name__=='__main__':
#     Read the configuration file
#     Set up email details
#     Initialize logging
#     Initialize email_sent flag
#     Call main function with arguments


get_ticket_info(STUBHUB_URL, TICKET_X_PATHS)