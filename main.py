import requests

# https://developer.nutritionix.com/
APP_ID = "6ce9ef66"
API_KEY = "111bfb0e20e2d02690ce5663b1df922a"

ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("What exercise did you complete?:  ")

params = {
    "query": exercise_text,
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url=ENDPOINT, json=params, headers=headers)
response.raise_for_status()
print(response.text)
