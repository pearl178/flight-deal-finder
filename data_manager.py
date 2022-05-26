import requests

class DataManager:
    def __init__(self):
        self.END_POINT = 'https://api.sheety.co/f266fc6da30b4c5d27abf38dbec08fea/flightDeals/prices'
        self.response = requests.get(url=f"{self.END_POINT}")
        self.rows = self.response.json()['prices']

    def get_city_names(self):
        city_names = [row['city'] for row in self.rows]
        return city_names

    def get_current_prices(self):
        city_code_current_price = {row['iataCode']: row['lowestPrice'] for row in self.rows}
        return city_code_current_price

    def fill_sheet_codes(self, city_codes):
        for n in range(len(city_codes)):
            sheety_parameters = {
                'price':
                    {
                        'iataCode': city_codes[n]
                    }
            }
            id_num = n + 2
            requests.put(url=f"{self.END_POINT}/{id_num}", json=sheety_parameters)