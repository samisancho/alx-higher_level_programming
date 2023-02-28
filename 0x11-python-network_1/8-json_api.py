#!/usr/bin/python3
import requests
from sys import argv
# http://21701fe1a6fd.19.hbtn-cod.io:5000/search_user


if __name__ == "__main__":
    if len(argv) == 2:
        url = "http://0.0.0.0:5000/search_user"
        payload = {}

        if argv[1]:
            payload['q'] = argv[1]
        else:
            payload['q'] = ""

        res = requests.post(url, data=payload)
        res.raise_for_status()

        try:
            obj = res.json()
            try:
                _id = "[{}] ".format(obj['id'])
                name = "{}".format(obj['name'])
                print(_id + name)
            except:
                print('No result')
        except:
            print('Not a valid JSON')
    else:
        print('No result')
