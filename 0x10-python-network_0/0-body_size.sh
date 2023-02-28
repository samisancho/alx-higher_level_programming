#!/bin/bash
# shot Content-Length of a response header from a request
curl -Is "$1" | grep "Content-Length:" | awk '{print $2}'
