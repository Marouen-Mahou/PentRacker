import requests
import os

from dotenv import load_dotenv

load_dotenv()
key = os.getenv('MAIL_GUN_KEY')
sandbox = os.getenv('MAIL_GUN_SANDBOX')


def send_email(code, email):

    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    recipient = email
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'PENTRACKER@gmail.com',
        'to': email,
        'subject': 'verification code',
        'text': 'your verification code is : {0}'.format(code)})



