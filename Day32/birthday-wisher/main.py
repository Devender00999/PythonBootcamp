##################### Extra Hard Starting Project ######################
import datetime as dt
import smtplib
import pandas
import random
from dotenv import load_dotenv
import os

load_dotenv()

# 2. Check if today matches a birthday in the birthdays.csv
df = pandas.read_csv('birthdays.csv')
birthdays = df.to_dict(orient="records")

today = dt.datetime.now()

# Choosing letters
letter_file = open(f'letter_templates/letter_{random.randint(1, 3)}.txt')
letter = letter_file.read()

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
   # except Exception:
   #    print('Could not send email.')
# se
for birthday in birthdays:
   if today.day == birthday['day'] and today.month == birthday['month']:
      send_mail(birthday['email'], 'Happy Birthday!!!', message=letter.replace('[NAME]', birthday['name']))



letter_file.close()


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




