from dotenv import load_dotenv
import os
import requests

load_dotenv()
API_KEY = os.environ.get('API_KEY')

params = {
   'lat': 12.971599,
   "lon": 77.594566,
   "appId": API_KEY,
   "cnt": 4
}
res = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=params)
res.raise_for_status()

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

data = res.json().get('list')
for i in data:
   weather = i['weather'][0]['id']
   if (weather > 700):
      send_mail('devender00999@gmail.com', 'Take an Umbrella', 'Hey Devender\n It may remain tomorrow, So take umbrella wherever you go.')
      break
   
