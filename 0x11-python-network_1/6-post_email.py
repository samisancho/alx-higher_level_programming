#!/usr/bin/python3
import requests
from sys import argv


if __name__ == "__main__":
    url = argv[1]
    email = argv[2]
    payload = {'email': email}

    res = requests.post(url, data=payload)
    print(res.text)
