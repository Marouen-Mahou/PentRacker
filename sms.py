import os

from dotenv import load_dotenv
from twilio.rest import Client



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

load_dotenv()

print(account_sid)
print(auth_token)

client = Client(account_sid, auth_token)


def send_verif(message, phone):
    message = client.messages \
        .create(
        body=" your Pentracker verification code is : '%s' " % (message),
        from_='+19147581161',
        to='+216' + phone
    )
