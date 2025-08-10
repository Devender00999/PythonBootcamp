import requests 
from dotenv import load_dotenv
import os
import datetime

load_dotenv()

NUTRITIONNIX_API = "https://trackapi.nutritionix.com/v2"
SHEETY_API = "https://api.sheety.co/051e988865886635a914163f1b472ee2/myWorkouts/workouts"
TOKEN = os.getenv('NUTRITIONNIX_API')
APP_ID = os.getenv('NUTRITIONNIX_APP_ID')
SHEETY_TOKEN = os.getenv('GENERIC_AUTH_TOKEN')

def get_excersize_data(query):
   headers = {
      'Content-Type': 'application/json',
      'x-app-id': APP_ID,
      'x-app-key': TOKEN,
   }

   data = { "query": query }

   response = requests.post(f"{NUTRITIONNIX_API}/natural/exercise", json=data, headers=headers)

   response.raise_for_status()
   return response.json()

sheety_headers = {
   'Content-Type': 'application/json',
   'Authorization': f"Bearer {SHEETY_TOKEN}"

}

def get_sheet_data():
   res = requests.get(f"{SHEETY_API}", headers=sheety_headers)
   res.raise_for_status()
   return res.json()
   
def add_data_to_sheet(data):
   res = requests.post(f'{SHEETY_API}', json={ "workout": data}, headers=sheety_headers)
   print(res.text)
   res.raise_for_status()
   return res.json()
   
# excer_data = {'date': '21/08/2020', 'time': '15:00:00', 'exercise': 'Running', 'duration': 22, 'calories': 130, 'id': 2}


# main program
excersize = input("Tell me which excersize you did? \n")

excer_data = get_excersize_data(excersize)
today = datetime.datetime.now()
if (len(excer_data['exercises']) == 0):
   print('Please add valid exercise')
else:
   for excersize in excer_data['exercises']:
      payload = {
         'date': today.strftime("%m/%d/%Y"), 
         'time': today.strftime("%H:%M:%S"), 
         'exercise': excersize['name'], 
         'duration': excersize['duration_min'], 
         'calories': excersize['nf_calories']
      }
      add_data_to_sheet(payload)
