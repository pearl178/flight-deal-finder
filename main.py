# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests

# TODO:Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
#  International Air Transport Association (IATA) codes for each city.

##Get city names as a list from google sheet
SHEETY_END_POINT = 'https://api.sheety.co/f266fc6da30b4c5d27abf38dbec08fea/flightDeals/prices'
sheety_response = requests.get(url=f"{SHEETY_END_POINT}")
rows = sheety_response.json()['prices']
city_names = [row['city']for row in rows]


TEQUILA_END_POINT = 'https://tequila-api.kiwi.com/locations/query'
header = {
    'apikey': 'gu3ZrG3H8OXk1DfvSb_22Rra1pJw-Wkf'
}
# Use a for loop to search for each city's city code and write into Google sheet
for n in range(len(city_names)):
    tequila_parameters = {
        'term': city_names[n],
        'location_types': 'city',
        'limit': 1
    }
    tequila_response = requests.get(url=TEQUILA_END_POINT, headers=header, params=tequila_parameters)
    city_code = tequila_response.json()['locations'][0]['code']

    sheety_parameters = {
        'price':
            {
                'iataCode': city_code
            }
        }
    id_num = n+2
    requests.put(url=f"{SHEETY_END_POINT}/{id_num}", json=sheety_parameters)
