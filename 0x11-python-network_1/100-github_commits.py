#!/usr/bin/python3
import requests
from sys import argv

if __name__ == "__main__":
    res = requests.get('https://api.github.com/repos/{}/{}/commits'.format(
        argv[2], argv[1]))

    obj = res.json()
    for el in obj[0:10]:
        sha = el['sha']
        author = el['commit']['author']['name']
        print("{}: {}".format(sha, author))
