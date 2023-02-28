#!/usr/bin/python3
import requests

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    res = requests.get(url)
    if res.status_code == 200:
        print('Body response:')
        print('\t- type: {}'.format(type(str(res))))
        print('\t- content: {}'.format(res.text))
