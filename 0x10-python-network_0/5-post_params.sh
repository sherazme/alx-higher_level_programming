#!/bin/bash
# script that displays the body of the response for given URL
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
