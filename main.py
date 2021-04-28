import requests
from twilio.rest import Client

account_sid = "ACd1dc43b2a16f4364690bb06b6abfd853"
auth_token = "432979e953131e796ef4d3dd62a59148"

OWN_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "82030ab691ee1bba0214fc1c0484834a"

weather_parameters = {
    "lat": 4.710989,
    "lon": -74.072090,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts"

}
response = requests.get(OWN_ENDPOINT, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"]
weather_slice = hourly_data[:12]

will_rain = False


for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:

        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)


    message = client.messages \
                    .create(
                         body="It's going to rain today. Remember to bring an ☔️.",
                         from_='+19705077060',
                         to='+2347068827272'
                     )

    print(message.status)
