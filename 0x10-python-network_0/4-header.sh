#!/bin/bash
# send a header variable with a request "X-HolbertonSchool-User-Id"
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
