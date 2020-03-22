#!/usr/bin/env python
import requests
import sys


def callTelegram(text):
    base_url = "https://api.telegram.org/"
    call_type = "bot"
    credentials = open("credentials.txt","r").read().split()
    print(credentials)
    verb = "/sendMessage"

    url = base_url + call_type + caller_id + verb

    query = "?chat_id="+channel_id+"&text="+text
    r = requests.post(url = url+ query)

if __name__ == "__main__":
    callTelegram(sys.argv[1])
