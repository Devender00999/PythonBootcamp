# getting data from API
import requests

# calling API
response = requests.get('http://api.open-notify.org/iss-now.json')

# raising exception
# response.raise_for_status()

# print(response.json())

params = {
   "lat": 36.7201600,
   'lng': -4.4203400,
   "formatted": 0
   
}
res = requests.get('https://api.sunrise-sunset.org/json', params=params)
print(res.json())