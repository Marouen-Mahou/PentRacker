import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "AC4f1d11f7bb5166966f5ac8b2b83ab8d2"
auth_token = "d22c2da5048cc6912f03cfb5fe2f994b"

client = Client(account_sid, auth_token)


def send_verif(message, phone):
    message = client.messages \
        .create(
        body=" your Pentracker verification code is : '%s' " % (message),
        from_='+19147581161',
        to='+216' + phone
    )
