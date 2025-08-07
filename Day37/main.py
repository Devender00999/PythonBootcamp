import requests
from dotenv import load_dotenv
import os


load_dotenv()
TOKEN = os.getenv('PIXELA_TOKEN')
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

# creating graph
graph_data = { "id": "test", "name": "Graph", "unit":"commit","type":"int","color":"shibafu"}
res = requests.post(URL + f"/{USERNAME}/graphs", json={ "id": "test", "name": "Graph", "unit":"commit","type":"int","color":"shibafu"}, headers={ "X-USER-TOKEN": TOKEN})
print(res.text)
