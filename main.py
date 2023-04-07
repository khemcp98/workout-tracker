import os
import requests
import datetime as dt

TOKEN = os.environ.get("TOKEN")
APP_ID = os.environ.get('api_id')
APP_KEY = os.environ.get("api_key")

date = dt.datetime.now().strftime("%x")
time = dt.datetime.now().strftime("%X")

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
    "Content-Type": "application/json"
}

query = input("what did you do: ")
params = {
    "query": query,
    "gender": "male",
    "weight_kg": 53,
    "height_cm": 172,
    "age": 24
}

response = requests.post(url=endpoint, headers=headers, json=params)
response.raise_for_status()
data = response.json()["exercises"]

sheety_endpoint = "https://api.sheety.co/98b80472ab3f60f9d50bdd2a76ff1b82/myWorkouts/workouts"
s_headers = {
    "Authorization": f"Bearer {TOKEN}"
}

for exercises in data:
    exercise_name = exercises["name"]
    exercise_duration = exercises["duration_min"]
    exercise_calories = exercises["nf_calories"]

    data_params = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_name.title(),
            "duration": exercise_duration,
            "calories": exercise_calories
        }
    }
    send_data = requests.post(url=sheety_endpoint, headers=s_headers, json=data_params)
    print(send_data.text)
