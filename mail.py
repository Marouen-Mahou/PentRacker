import requests

key = '548bd0d958e911ef9ab0be9d6c8fa81e-24e2ac64-94e69bcd'
sandbox = 'sandbox4e4467e881824450bcb2ed4ff368fa49.mailgun.org'


def send_email(code, email):
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    recipient = email
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'PENTRACKER@gmail.com',
        'to': recipient,
        'subject': 'verification code',
        'text': 'your verification code is : {0}'.format(code)})
    print(request)
