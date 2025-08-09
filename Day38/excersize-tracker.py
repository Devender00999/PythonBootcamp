import requests 
from dotenv import load_dotenv
import os

load_dotenv()

NUTRITIONNIX_API = "https://trackapi.nutritionix.com/v2"
TOKEN = os.getenv('NUTRITIONNIX_API')
APP_ID = os.getenv('NUTRITIONNIX_APP_ID')

headers = {
   'Content-Type': 'application/json',
   'x-app-id': APP_ID,
   'x-app-key': TOKEN,
}

data = {
   "query": "I ran 5KM for 30 Minutes"
}
# print(headers)
# response = requests.post(f"{NUTRITIONNIX_API}/natural/exercise", json=data, headers=headers)
# print(response.url)
# print(response.text)

SHEETY_API = "https://api.sheety.co/051e988865886635a914163f1b472ee2/myWorkouts/workouts"
res = requests.get(f"{SHEETY_API}")
print(res.json())