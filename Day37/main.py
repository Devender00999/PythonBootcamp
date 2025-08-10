import requests
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('GENERIC_AUTH_TOKEN')
USERNAME = os.getenv('USERNAME')

# creating a user
URL = 'https://pixe.la/v1/users'

# data = {
#    "token": TOKEN,
#    "username": "andrewsmith",
#    "agreeTermsOfService": "yes",
#    "notMinor": "yes"
# }
# res = requests.post(URL, json=data)
# print(res.reason)
# print(res.json())

headers = { "X-USER-TOKEN": TOKEN }
# creating graph
# graph_data = { "id": "test", "name": "Graph", "unit":"commit","type":"int","color":"shibafu"}
# res = requests.post(URL + f"/{USERNAME}/graphs", json={ "id": "test", "name": "Graph", "unit":"commit","type":"int","color":"shibafu"}, headers=headers)
# print(res.text)

# posting a streak on the pixela
commit_data = { "unit": "Kms"}
# res = requests.post(f"{URL}/{USERNAME}/graphs/test", json=commit_data, headers=headers)
# print(res.text)


# updating data 
# res = requests.put(f"{URL}/{USERNAME}/graphs/test", json=commit_data, headers=headers)
# print(res.text)

# deleting data
# res = requests.delete(f"{URL}/{USERNAME}/graphs/test", headers=headers)
# print(res.text)


