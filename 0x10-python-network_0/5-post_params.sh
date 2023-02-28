#!/bin/bash
# script that sendt a request  POST wuth variables
curl -s "$1" -X POST -d "email=hr@holbertonschool.com" -d "subject=I will always be here for PLD"
