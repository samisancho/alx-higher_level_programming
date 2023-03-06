#!/usr/bin/python3

import requests
from base64 import urlsafe_b64encode
from sys import argv


def get_bearer_token(apiKey, secretKey, searchSt):
    """ Get the bearer token from url passed a argument [2] """

    bearerToken = '{}:{}'.format(apiKey, secretKey)
    Token = urlsafe_b64encode(bearerToken.encode('ascii')).decode('ascii')

    data = {"grant_type": "client_credentials"}
    headers = {"Authorization": "Basic {}".format(
        Token),
        "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"}

    accessToken = post_request(headers, data)
    tweets = get_request(accessToken, searchSt)

    list_tweets = tweets.get('statuses')
    return list_tweets


def post_request(headers, data):
    """ send a post request with data to get access token"""

    authUrl = 'https://api.twitter.com/oauth2/token'
    res = requests.post(authUrl, headers=headers, data=data)
    to_json = res.json()
    accessToken = to_json['access_token']
    return accessToken


def get_request(accessToken, searchSt):
    """ Send a get request to the twitter ap to get tweets """

    url = 'https://api.twitter.com/1.1/search/tweets.json'
    headers = {"Authorization": "Bearer {}".format(accessToken)}
    params = {'q': searchSt, 'result_type': 'recent', 'count': 5}

    res = requests.get(url, headers=headers, params=params)
    tweets = res.json()
    return tweets


if __name__ == "__main__":

    list_tweets = get_bearer_token(argv[1], argv[2], argv[3])

    for el in list_tweets:
        _id = el['id']
        text = el['text']
        username = el['user']['name']
        print('[{}] {} by {}'.format(_id, text, username))
