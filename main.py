import requests
import credentials
from datetime import datetime

# TODO 1: Use nutrition api to parse the text :

NUTRITION_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": credentials.NUTRITION_APP_ID,
    "x-app-key": credentials.NUTRITION_API_KEY
}
user_action = input("What did you do today? ")

PARAMS = {
    "query": user_action,
    "gender": "male",
    "weight_kg": 57,
    "height_cm": 155,
    "age": 26
}

response = requests.post(url=NUTRITION_END_POINT, json=PARAMS, headers=HEADERS)
response_data = response.json()

# TODO 2: Add the data the spreadsheet
SHEET_END_POINT = "https://api.sheety.co/8985bc8d160f1e1e3c7249582836a018/myActivities/sheet1"
bearer_headers = {
    "Authorization": credentials.BEARER_AUTH
}
for index in range(len(response_data['exercises'])):
    data_to_add = {
        "sheet1": {
            "date": datetime.strftime(datetime.now(), "%Y-%m-%d"),
            "time": datetime.strftime(datetime.now(), "%H:%M:%S"),
            "exercise": response_data['exercises'][index]['user_input'],
            "duration": response_data['exercises'][index]['duration_min'],
            "calories": response_data['exercises'][index]['nf_calories']
        }
    }
    response = requests.post(url=SHEET_END_POINT, json=data_to_add, headers=bearer_headers)
