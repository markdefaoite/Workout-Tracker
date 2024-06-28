from datetime import datetime
import os
import requests

# https://developer.nutritionix.com/
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
POST_WORKOUT_SHEETY = "https://api.sheety.co/7089274e21f47622530dd4c143cf9f22/myWorkouts/workouts"
AUTHORIZATION = os.environ["AUTHORIZATION"]

exercise_text = input("What exercise did you complete?:  ")
today = datetime.now()

params = {
    "query": exercise_text,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

sheety_headers = {
    "Authorization": AUTHORIZATION
}

response = requests.post(url=NUTRITIONIX_ENDPOINT, json=params, headers=headers)
response.raise_for_status()


data = response.json()["exercises"]

for exercise in data:
    sheet_inputs = {
        "workout": {
            "date": str(today.strftime("%d/%m/%Y")),
            "time": str(today.strftime("%H:%M:%S")),
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(POST_WORKOUT_SHEETY, json=sheet_inputs, headers=sheety_headers)

