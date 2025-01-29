# Price Check Ticket Bot 🎟

Automated Stubhub ticket price checking

## Description

An in-depth paragraph about your project and overview of use.

### Features
- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3


### Built With
* [![Python][Python][Python-url]]
* [![Selenium][Selenium][Selenium-url]]
* [![Twilio][Twilio][Twilio-url]]
* [![stmplib][stmplib][stmplib-url]]


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

### Executing program

* Running locally:
```
python {path to file}/ticket_bot.py
```

## Acknowledgments

Thanks to the following sources for guidance/inspiration
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