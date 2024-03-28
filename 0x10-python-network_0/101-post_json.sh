#!/bin/bash 
# script that displays body of the response from given URL
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
