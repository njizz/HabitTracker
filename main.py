import requests
import json
from datetime import datetime

with open("config.json") as json_data_file:
    config_data = json.load(json_data_file)

USERNAME = config_data['username']
TOKEN = config_data['token']
GRAPH_ID = "pushup20"

pixela_endpoint = "https://pixe.la/v1/users"
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_params = {
    "id": "GRAPH_ID",
    "name": "Push-up Graph",
    "unit": "push-ups",
    "type": "int",
    "color": "momiji"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# -----INITIAL SETUP ONLY-----
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# -----GRAPH SETUP ONLY-----
# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

pixel_date = datetime.strftime(datetime.now(), "%Y%m%d")
quantity = "20"

pixel_params = {
    "date": pixel_date,
    "quantity": quantity
}

# -----PIXEL CREATION-----
# response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

update_endpoint = f"{pixel_endpoint}/{pixel_date}"

new_pixel_data = {
    "quantity": "25"
}

# -----UPDATE A PIXEL-----
response = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)
print(response.text)

# -----DELETE A PIXEL-----
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)
