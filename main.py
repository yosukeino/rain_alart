import requests
from twilio.rest import Client

api_key = ""
OWM_Endpoint = ""

# TWILIO THINGS
account_sid = ''
auth_token = ''


weather_params = {
    "lat": 36.549980,
    "lon": 139.870010,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall",
                        params=weather_params)
response.raise_for_status()
data = response.json()
weather_slice = data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message=client.messages.create(
        messaging_service_sid='',
        body='today is raining',
        to='+817045532745'
        )

print(message.status)
