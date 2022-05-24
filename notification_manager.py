import requests
from twilio.rest import Client

class NotificationManager:
    def __init__(self):
        self.account_sid = 'AC5291353c75429cc516071c422886464f'
        self.auth_token = '4a52811e3dfb6ee416505f6ab2bc8594'

    def send_message(self):
        message_to_send = "LOW PRICE!!!"
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=message_to_send,
            from_='+14707858749',
            to='+18017590187'
        )
        print(message.status)