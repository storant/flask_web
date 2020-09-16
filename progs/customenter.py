#upload mp3 for ncco on this website https://www.mailboxdrive.com/

import nexmo
from pprint import pprint
from progs.time import curr_time
from progs.mongodb import table_load
from progs.logins import nexmo_logins
#from progs.get_key import get_key

#when uploading to python anywhere, change 
# private_key='private.key'
# because it looks in a different locations

nexmo_logins = nexmo_logins()
client = nexmo.Client(
  application_id = nexmo_logins['app_id'],
  private_key='progs/private.key',
  key = nexmo_logins['key'], 
  secret = nexmo_logins['secret']
)
#voice = nexmo.Voice(client)
#sms = nexmo.Sms(client)

#pull the current account number
accnumbers = client.get_account_numbers()
nexnum = accnumbers['numbers'][0]['msisdn']

def get_number():
    return nexnum


def get_balance():
    result = client.get_balance()
    #print(result)
    return (f"{result['value']} EUR")


def send_message(num, msg):
    response = client.send_message({
    'from': nexnum,
    'to': num,
    'text': msg})
    #print(response['message-id'])
    #pprint(response)

def send_message_two(num, msg):
    response = client.send_message({
        'from': nexnum,
        'to': num,
        'text': msg})
    #pprint(response)
    #loading the table
    message_id = response['messages'][0]['message-id']
    price = response['messages'][0]['message-price'] 
    remaining_balance = response['messages'][0]['remaining-balance'] 
    time = curr_time()
    table_load(time,message_id,nexnum,num,msg,price,remaining_balance)

def send_call(num,msg):
    ncco = [{
        'action': 'talk',
        'voiceName': 'Kendra',
        'text': msg}]
    response = client.create_call({
        'to': [{
            'type': 'phone',
            'number': num}],
        'from': {
            'type': 'phone',
            'number': nexnum},
        'ncco' : ncco})
    #print(response['uuid'])
    #pprint(response)

def ricktwo(num):
    ncco = [{
        "action": "stream",
        "streamUrl": ["https://www.mboxdrive.com/cut_Rick%20Astley%20Never%20gonna%20give%20you%20up%20%20(mp3cut.net).mp3"]
        }]
    response = client.create_call({
        'to': [{
            'type': 'phone',
            'number': num}],
        'from': {
            'type': 'phone',
            'number': nexnum},
        'ncco' : ncco})
    #print(response['uuid'])
    #pprint(response)

