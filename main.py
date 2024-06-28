from datetime import datetime

import requests

# https://developer.nutritionix.com/
APP_ID = "6ce9ef66"
API_KEY = "111bfb0e20e2d02690ce5663b1df922a"
NUTRITIONIX_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

POST_WORKOUT_SHEETY = "https://api.sheety.co/7089274e21f47622530dd4c143cf9f22/myWorkouts/workouts"

exercise_text = input("What exercise did you complete?:  ")
today = datetime.now()

params = {
    "query": exercise_text,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
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

    sheet_response = requests.post(POST_WORKOUT_SHEETY, json=sheet_inputs)

    print(sheet_response.text)
