#!/bin/bash
# see the avaliable options to request this server url
curl -Is "$1" | grep "Allow:" | cut -d " " -f2-
