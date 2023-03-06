#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":

    res = requests.get("https://api.github.com/user", auth=(argv[1], argv[2]))

    try:
        obj = res.json()
        _id = obj.get('id')
        print(_id)
    except:
        print("None")
