import requests

key = 'key-6b19b84742cc60117659f606330f43ff'
sandbox = 'sandbox4e4467e881824450bcb2ed4ff368fa49.mailgun.org'


def send_email(code, email):
    request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
    recipient = email
    request = requests.post(request_url, auth=('api', key), data={
        'from': 'PENTRACKER@gmail.com',
        'to': "benslamasouheil@gmail.com",
        'subject': 'verification code',
        'text': 'your verification code is : {0}'.format(code)})


send_email(201, "benslamasouheil@gmail.com")