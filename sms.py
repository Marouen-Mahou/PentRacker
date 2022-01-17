import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC4f1d11f7bb5166966f5ac8b2b83ab8d2"
auth_token = "b43d2f43f3aa10fcfed5a3032954dc81"
client = Client(account_sid, auth_token)

def send_verif(message,phone) :
        message = client.messages \
                .create(
                     body=message,
                     from_='+19147581161',
                     to='+216'+phone
                 )