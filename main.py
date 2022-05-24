# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests
import datetime as dt

TEQUILA_END_POINT = 'https://tequila-api.kiwi.com/'
header = {
    'apikey': 'gu3ZrG3H8OXk1DfvSb_22Rra1pJw-Wkf'
}


# TODO 1: Use the Flight Search and Sheety API to populate your own copy of the Google Sheet with
#  International Air Transport Association (IATA) codes for each city.

# Get city names as a list from google sheet
SHEETY_END_POINT = 'https://api.sheety.co/f266fc6da30b4c5d27abf38dbec08fea/flightDeals/prices'
sheety_response = requests.get(url=f"{SHEETY_END_POINT}")
rows = sheety_response.json()['prices']
city_names = [row['city']for row in rows]
city_codes = []

# Use a for loop to search for each city's city code and write into Google sheet
for n in range(len(city_names)):
    tequila_parameters = {
        'term': city_names[n],
        'location_types': 'city',
        'limit': 1
    }
    tequila_response = requests.get(url=f"{TEQUILA_END_POINT}locations/query", headers=header, params=tequila_parameters)
    city_code = tequila_response.json()['locations'][0]['code']
    city_codes.append(city_code)

    sheety_parameters = {
        'price':
            {
                'iataCode': city_code
            }
        }
    id_num = n+2
    requests.put(url=f"{SHEETY_END_POINT}/{id_num}", json=sheety_parameters)

# TODO 2: Use the Flight Search API to check for the cheapest flights from tomorrow to 6 months later for all
#  the cities in the Google Sheet.
# Get the date range (60 days from tomorrow)
date_from = dt.date.today() + dt.timedelta(days=1)
date_to = dt.date.today() + dt.timedelta(days=60)
date_from = date_from.strftime('%d/%m/%Y')
date_to = date_to.strftime('%d/%m/%Y')

city_code_price = {}
for city_code in city_codes:
    search_parameters = {
        'fly_from': 'LON',
        'fly_to': city_code,
        'date_from': date_from,
        'date_to': date_to,
        'limit': 1
    }
    response = requests.get(url=f"{TEQUILA_END_POINT}search", headers=header, params=search_parameters)
    price = response.json()['data'][0]['price']
    city_code_price[city_code] = price

print(city_code_price)
# TODO 3: If the price is lower than the lowest price listed in the Google Sheet then send an SMS to your own number
#  with the Twilio API.



# TODO 4: The SMS should include the departure airport IATA code, destination airport IATA code, departure city,
#  destination city, flight price and flight dates. e.g.


