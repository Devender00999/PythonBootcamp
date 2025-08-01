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
data = res.json().get('list')
for i in data:
   weather = i['weather'][0]['id']
   if (weather > 700):
      print('Bring an Umbrella.')
      break