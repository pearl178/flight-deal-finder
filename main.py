from notification_manager import NotificationManager
from data_manager import DataManager
from flight_data import FlightData
from flight_search import FlightSearch


data_manager = DataManager()
flight_data = FlightData()
notification = NotificationManager()
flight_search = FlightSearch()


city_names = data_manager.get_city_names()
city_codes = flight_data.get_city_codes(city_names)
data_manager.fill_sheet_codes(city_codes)
city_code_current_price = data_manager.get_current_prices()


for city_code in city_codes:
    flight_info = flight_search.get_lowest_price(city_code)
    price = flight_info['price']
    if price < city_code_current_price[city_code]:
        notification.send_message(flight_info)


