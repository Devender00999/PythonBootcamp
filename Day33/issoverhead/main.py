import requests
from datetime import datetime
import smtplib
import os
from dotenv import load_dotenv
import time

load_dotenv()

MY_LAT = 12.9069795 # Your latitude
MY_LONG = 77.6422078 # Your longitude



def is_iss_over_my_home():
   response = requests.get(url="http://api.open-notify.org/iss-now.json")
   response.raise_for_status()
   data = response.json()

   iss_latitude = float(data["iss_position"]["latitude"])
   iss_longitude = float(data["iss_position"]["longitude"])
   if (MY_LAT - 5 >= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 >= iss_longitude <= MY_LONG + 5):
      return True
   return False

#Your position is within +5 or -5 degrees of the ISS position.


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Asia/Kolkata"
}

def is_dark():
   response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
   response.raise_for_status()
   data = response.json()
   sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
   sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

   time_now = datetime.now()
   current_hour = time_now.hour
   return current_hour < sunrise and current_hour > sunset


   


#If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.

def send_email_to_lookup():
   if is_iss_over_my_home() and is_dark():
      send_mail('devender00999@gmail.com', 'ISS Notification', 'Look Up \n ISS is over your home.')
# BONUS: run the code every 60 seconds.

# to sending email
def send_mail(email, subject,  message):
# try: 
   with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
   # start tls for security
      connection.starttls()

      email = os.getenv('EMAIL')
      password = os.getenv('PASSWORD')
      
      # login in current account
      connection.login(user=email, password=password)
      print("Sending Email...")
      
      # sending email 
      connection.sendmail(from_addr=email, to_addrs=email, msg=f"Subject:{subject}\n\n{message}")
      print("Email sent successfully.")


while True:
   time.sleep(60)
   send_email_to_lookup()
   




