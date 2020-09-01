#!/usr/bin/env python
import tweepy, sys, time
from random import randint
from keys import keys
import subprocess
import json
import time

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

def set_up():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    return api

def getUserDetails():
    h = subprocess.call('./getFriends.sh')
    with open('./ids.txt') as f:
        ids = f.readlines()
        ids = ids[0].split(",")
    return ids

def send_message(api, ids):
    prev_id = 0
    msg_id = 0

    for id in ids:
        m = sys.argv[1]
        # s = api.update_status(m)
        api.send_direct_message(id, "Hello message")

    while (1):

        last_dms = api.list_direct_messages(count=50)
        print("NEW TIME NEW TIME")
        print(last_dms)
        print("NEW TIME NEW TIME")

        for dm in last_dms:
            print(dm.message_create['message_data']['text'])
            recipient = (dm.message_create['target']['recipient_id'])
            sender = (dm.message_create['sender_id'])
            prev_id = msg_id
            msg_id = dm.id
            print(recipient)
            print(type(sender))
            if (int(sender) != 1299796326952116224) and (prev_id != msg_id):
                message = (dm.message_create['message_data']['text'])
                break
        print(message)
        print(prev_id)
        print(msg_id)
        if msg_id != prev_id:
            api.send_direct_message(id, "User sent message:" + message + "\n")

        if message == "bye":
            break

        time.sleep(100)
        print("end of new time")

api = set_up()
ids = getUserDetails()
send_message(api, ids)
