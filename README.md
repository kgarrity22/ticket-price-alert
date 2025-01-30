# Ticket Price Alert Bot 🎟

Automated Stubhub ticket price checking with python & selenium

## Description
This project was created to programatically check ticket prices on stubhub for the Big East championship game. It uses selenium webdriver to navigate to the ticketing page and locate and read xml elements. If the ticket price is below a specified threshold, an automated email is then sent to notify the user. 
You can adapt this ticket bot for your own use by modifying the ticket url, element xpaths, email content, and price threshold.

### What's in here
- `ticket_bot.py` ➡️ this file is home to the main bot functionality - the webdriver navigation, the price checking, and the final email notification process
- `send_email.py` ➡️ generic function for sending an email with stmplib
- `send_sms.py` ➡️ generic function for sending an sms message with twilio 


### Built With
* [![Python][Python]][Python-url]
* [![Selenium][Selenium]][Selenium-url]
* [![Twilio][Twilio]][Twilio-url]
* [![stmplib][stmplib]][stmplib-url]


## Getting Started

### Dependencies

* See `requirements.txt` for dependencies

### How to use


1. Clone the repo
   ```sh
   git clone https://github.com/kgarrity22/ticket-price-alert
   ```
2. Install dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. In `ticket_bot.py` replace the constant values with your own desired ticket info (`STUBHUB_URL`, `TICKET_X_PATHS`, `EMAIL_SUB`, `PRICE_THRESHOLD`) 
4. Create your own `keys.py` file with the following (if you wish to send & receive email notifications):
* `SENDER_EMAIL` 
* `SENDER_PASSWORD`
* `RECEIVER_EMAIL`
- for SENDER_PASSWORD with gmail, you'll need to create an [app password](https://knowledge.workspace.google.com/kb/how-to-create-app-passwords-000009237)
If you have an active Twilio account you can also define the following in order to receive notifications via text:
* `TWILIO_ACCOUNT_ID`
* `TWILIO_AUTH_TOKEN`
* `TWILIO_NUMBER`
* `CELL_NUMBER`

##### Running the check on a schedule
If you want to schedule the program to run, you can set up a [cron job](https://en.wikipedia.org/wiki/Cron) on your machine
ex. Check the ticket price each day at 8:
```
0 8 * * * python3 /path/to/ticket_bot.py
```

### Executing program

* Running locally:
```
python {your path to file}/ticket_bot.py
```

## Acknowledgments

Thanks to the following sources for guidance/inspo:
* [https://medium.com/@benlahner/how-to-build-your-own-ticket-bot-63c3d0706e92](https://medium.com/@benlahner/how-to-build-your-own-ticket-bot-63c3d0706e92)
* [https://mailtrap.io/blog/python-send-email-gmail/](https://mailtrap.io/blog/python-send-email-gmail/)



[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python
[Python-url]: https://www.python.org/
[Selenium]: https://img.shields.io/badge/selenium-000000?style=for-the-badge&logo=selenium
[Selenium-url]: https://www.selenium.dev/
[Twilio]:https://img.shields.io/badge/twilio-000000?style=for-the-badge&logo=twilio
[Twilio-url]:https://www.twilio.com/en-us 
[stmplib]: https://img.shields.io/badge/stmplib-000000?style=for-the-badge&logo=stmplib
[stmplib-url]: https://docs.python.org/3/library/smtplib.html
