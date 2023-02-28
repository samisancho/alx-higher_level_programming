#!/usr/bin/python3
from urllib import request
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    with request.urlopen(url) as response:
        headers = response.info()
        if headers['X-Request-Id']:
            print(headers['X-Request-Id'])
