#!/bin/bash
# This script use curl
curl -sX POST -H "Content-Type: application/json" -d @./"$2" "$1"
