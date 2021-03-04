import requests
from twilio.rest import Client

endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "aaa7864ad19eae0091a285095e70f464"

# Your Account Sid and Auth Token from twilio.com/console
account_sid = "Your TWILIO_ACCOUNT_SID"
auth_token = "Your TWILIO_AUTH_TOKEN"

weather_params = {
    "lat": -24.814310,
    "lon": -65.435890,
    "appid": api_key
}

response = requests.get(endpoint, params=weather_params)
# print(response.status_code)
# print(response.json())
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"])
weather_slice = weather_data["hourly"][:12]
will_it_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    # print(condition_code)
    if condition_code < 700:
        will_it_rain = True

if will_it_rain:
    # print("Bring an Umbrella")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. Bring an Umbrella ☂️",
        from_='+98286577544',
        to='+919997654329'
    )



"""
Supported links:

https://home.openweathermap.org/
https://openweathermap.org/current
https://home.openweathermap.org/api_keys
https://openweathermap.org/api/one-call-api

https://httpstatuses.com/

Find Lat/Long: https://www.latlong.net/
Find where it is raining Currently: https://www.ventusky.com/

https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2

https://www.twilio.com/try-twilio
https://www.twilio.com/docs/sms/quickstart/python


www.pythonanywhere.com/
https://help.pythonanywhere.com/pages/TwilioBehindTheProxy/
"""