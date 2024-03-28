#!/bin/bash 
# script that displays only the status code of the responsefrom given URL
curl -s -L -X HEAD -w "%{http_code}" "$1"
