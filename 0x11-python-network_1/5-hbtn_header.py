#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get(argv[1])
    x_request_id = res.headers.get('X-Request-Id')
    print(x_request_id)
