import datetime as dt
import requests
class FlightSearch:
    def __init__(self):
        self.END_POINT = 'https://tequila-api.kiwi.com/'
        self.header = {
            'apikey': 'gu3ZrG3H8OXk1DfvSb_22Rra1pJw-Wkf'
        }
        date_from = dt.date.today() + dt.timedelta(days=1)
        date_to = dt.date.today() + dt.timedelta(days=60)
        self.date_from = date_from.strftime('%d/%m/%Y')
        self.date_to = date_to.strftime('%d/%m/%Y')

    def get_lowest_price(self, city_code):
        search_parameters = {
            'fly_from': 'LON',
            'fly_to': city_code,
            'date_from': self.date_from,
            'date_to': self.date_to,
            'limit': 1
        }
        response = requests.get(url=f"{self.END_POINT}search", headers=self.header, params=search_parameters)
        flight_info = response.json()['data'][0]
        return flight_info