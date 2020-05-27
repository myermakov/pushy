import requests
import urllib
import urllib.parse


import copy

import toml


print('loading config and user base...')
payload_template = toml.load('config.toml')
user_phones = toml.load('catalog.toml')


def get_templated_insult(insult_template=None):
    if not insult_template:
        insult_template = { 'template': 'Such <adjective>, much <adjective>!' } 

    args = urllib.parse.urlencode(insult_template).encode('ascii')
    response = requests.get('https://insult.mattbas.org/api/insult.json?', params=args)

    if response.status_code != 200:
        raise Exception(f'I got {response.status_code} instead of 200.')


    data = response.json()
    if data['error'] == True:
        raise Exception(f"Insult service error:\n{data['error_message']}.")

    insult = response.json().get('insult')

    if not insult:
        raise Exception("I didn't get properly insulted.")

    return insult


def make_message(msg: str, phone: str):
    print(msg)
    print(phone)

    payload = copy.deepcopy(payload_template)
    payload.update({'Message': msg, 'PhoneNumbers': phone})
    print(payload)
    return payload


def send_message(payload):
    #args = urllib.parse.urlencode(payload).encode('ascii')
    args = urllib.parse.urlencode(payload)
    print(args)
    response = requests.post('https://app.eztexting.com/sending/messages' , params=args)
    response = response.json()
    print(response)

  
if __name__ == '__main__':

    try:
        insult = get_templated_insult()
        print(insult)
        
        payload = make_message(msg=insult, phone=user_phones['lenti'])

        print(f"about to send \n\t *{insult}* \n to \n\t{payload['PhoneNumbers']}.")

        send_message(payload)

    except Exception as e: 
        print(e)





