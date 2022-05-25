import requests
from twilio.rest import Client
import datetime as dt

class NotificationManager:
    def __init__(self):
        self.account_sid = 'AC5291353c75429cc516071c422886464f'
        self.auth_token = '4a52811e3dfb6ee416505f6ab2bc8594'

    def send_message(self, info):
        departure_time = dt.datetime.fromtimestamp(info['dTime'])
        message_to_send = f"LOW PRICE!!!\n" \
                          f"Only ${info['price']} for flight from {info['cityFrom']}-{info['flyFrom']} to " \
                          f"{info['cityTo']}-{info['flyTo']} on {departure_time}"
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=message_to_send,
            from_='+14707858749',
            to='+18017590187'
        )
        print(message.status)