import requests

class FlightData:
    def __init__(self):
        self.END_POINT = 'https://tequila-api.kiwi.com/'
        self.header = {
        'apikey': 'gu3ZrG3H8OXk1DfvSb_22Rra1pJw-Wkf'
            }
        self.city_codes = []

    def get_city_codes(self, city_names):
        for n in range(len(city_names)):
            tequila_parameters = {
                'term': city_names[n],
                'location_types': 'city',
                'limit': 1
            }
            tequila_response = requests.get(url=f"{self.END_POINT}locations/query", headers=self.header,
                                            params=tequila_parameters)
            city_code = tequila_response.json()['locations'][0]['code']
            self.city_codes.append(city_code)
        return self.city_codes