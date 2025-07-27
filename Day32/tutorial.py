import smtplib
import datetime as dt
import random
from dotenv import load_dotenv
import os

load_dotenv()

import smtplib
# creating connection with gmail smtp server
def send_mail(email, subject,  message):
   with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
   # start tls for security
      connection.starttls()

      username = os.getenv('EMAIL')
      password = os.getenv('PASSWORD')

      # login in current account
      connection.login(user=username, password=password)
      print("Sending Email...")
      # sending email 
      connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:{subject}\n\n{message}")
      print("Email sent successfully.")

#
weekday = 6
def send_monday_quotes():
   today = dt.datetime.now()
   with open('quotes.txt') as file:
      quotes = file.readlines()
      quote_of_the_day = random.choice(quotes)
   if (today.weekday() == weekday):
      send_mail(email="devender@gmail.com", subject='Monday motivation.', message=quote_of_the_day)

# getting current time and day
# print(dt.datetime.now().year)


# creating custom date 
# date = dt.datetime(year=1995, month=12, day=21, hour=12, minute=34, second=34)
# print(date)
 
send_monday_quotes()

